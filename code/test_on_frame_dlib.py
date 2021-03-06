from PIL import Image
import argparse
import cv2
import datasets
import dlib
import hopenet
from hopenet import *
import os
import sys
import timeit
import torch
from torch.autograd import Variable
import torch.backends.cudnn as cudnn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
import utils

def parse_args():
  """Parse input arguments."""
  parser = argparse.ArgumentParser(description='Head pose estimation using the Hopenet network.')
  parser.add_argument('--gpu', dest='gpu_id', help='GPU device id to use [0]',
                      default=0, type=int)
  parser.add_argument('--snapshot', dest='snapshot', help='Path of model snapshot.',
                      default='', type=str)
  parser.add_argument('--face_model', dest='face_model', help='Path of DLIB face detection model.',
                      default='', type=str)
  parser.add_argument('--video', dest='video_path', help='Path of video')
  parser.add_argument('--output_string', dest='output_string', help='String appended to output file', default="")
  parser.add_argument('--frame', dest='frame', help='The frame to calculate', type=int, default=1)
  parser.add_argument('--conf_threshold', dest='conf_threshold', help='The face detection threshold', type=float, default=0.75)
  
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  args = parse_args()

  startTime = timeit.default_timer()
  
  print(torch.cuda.get_device_name(args.gpu_id))

  cudnn.enabled = True

  batch_size = 1
  gpu = args.gpu_id
  snapshot_path = args.snapshot
  out_dir = '../output'
  video_path = args.video_path

  if not os.path.exists(out_dir):
    os.makedirs(out_dir)

  if not os.path.exists(args.video_path):
    sys.exit('Video does not exist')

  # ResNet50 structure
  model = Hopenet(torchvision.models.resnet.Bottleneck, [3, 4, 6, 3], 66)

  # Dlib face detection model
  cnn_face_detector = dlib.cnn_face_detection_model_v1(args.face_model)

  print ('Loading snapshot.')
  # Load snapshot
  saved_state_dict = torch.load(snapshot_path)
  model.load_state_dict(saved_state_dict)

  print ('Loading data.')

  transformations = transforms.Compose([transforms.Scale(224),
                                       transforms.CenterCrop(224), transforms.ToTensor(),
                                       transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

  model.cuda(gpu)

  print ('Ready to test network.')

  # Test the Model
  model.eval()  # Change model to 'eval' mode (BN uses moving mean/var).
  total = 0

  idx_tensor = [idx for idx in range(66)]
  idx_tensor = torch.FloatTensor(idx_tensor).cuda(gpu)

  video = cv2.VideoCapture(video_path)

  txt_out = open(out_dir + '/output.txt', 'a+')
  
  # INFO
  txt_out_info = open(out_dir + '/info.txt', 'w')
  txt_out_info.write('DLIB model = %s\n' % (args.face_model))
  txt_out_info.write('pretrain model = %s\n' % (args.snapshot))


  print ("== Frame " + str(args.frame) + " == ")
  
  video.set(1, args.frame - 1) #we go to the determined image on the video
  ret, frame = video.read()
  if ret != False:
    
    cv2_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Dlib detect
    startDLIB = timeit.default_timer()
    print("-- Dlib Face detector")
    dets = cnn_face_detector(cv2_frame, 1)
    print("   Time : " + str(timeit.default_timer() - startDLIB))

    for idx, det in enumerate(dets):
      # Get x_min, y_min, x_max, y_max, conf
      x_min = det.rect.left()
      y_min = det.rect.top()
      x_max = det.rect.right()
      y_max = det.rect.bottom()
      conf = det.confidence

      print("Possible face (", x_min, ",", y_min, ",", x_max, ",", y_max, ") with", conf, "confidence ")

      conf_threshold = args.conf_threshold # threshold for visage detection (to modify and put in parameter)
      if conf > conf_threshold:
        print("-- Visage detected")
        print("-- Calculation of orientation")
        startVisage = timeit.default_timer()

        bbox_width = abs(x_max - x_min)
        bbox_height = abs(y_max - y_min)
        x_min -= 2 * bbox_width / 4
        x_max += 2 * bbox_width / 4
        y_min -= 3 * bbox_height / 4
        y_max += bbox_height / 4
        x_min = max(x_min, 0); y_min = max(y_min, 0)
        x_max = min(frame.shape[1], x_max); y_max = min(frame.shape[0], y_max)
        # Crop image
        img = cv2_frame[int(y_min):int(y_max), int(x_min):int(x_max)]
        img = Image.fromarray(img)

        # Transform
        img = transformations(img)
        img_shape = img.size()
        img = img.view(1, img_shape[0], img_shape[1], img_shape[2])
        img = Variable(img).cuda(gpu)

        yaw, pitch, roll = model(img)

        yaw_predicted = F.softmax(yaw, dim=1)
        pitch_predicted = F.softmax(pitch, dim=1)
        roll_predicted = F.softmax(roll, dim=1)
        # Get continuous predictions in degrees.
        yaw_predicted = torch.sum(yaw_predicted.data[0] * idx_tensor) * 3 - 99
        pitch_predicted = torch.sum(pitch_predicted.data[0] * idx_tensor) * 3 - 99
        roll_predicted = torch.sum(roll_predicted.data[0] * idx_tensor) * 3 - 99
        print("   Time : " + str(timeit.default_timer() - startVisage))

        # Print new frame with cube and axis
        txt_out.write(str(args.frame) + ' %f %f %f\n' % (yaw_predicted, pitch_predicted, roll_predicted))
        print("-- Result : ", yaw_predicted, pitch_predicted, roll_predicted)
        # utils.plot_pose_cube(frame, yaw_predicted, pitch_predicted, roll_predicted, (x_min + x_max) / 2, (y_min + y_max) / 2, size = bbox_width)
        utils.draw_axis(frame, yaw_predicted, pitch_predicted, roll_predicted, tdx=(x_min + x_max) / 2, tdy=(y_min + y_max) / 2, size=bbox_height / 2)
        # Plot expanded bounding box
        # cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0,255,0), 1)

  video.release()
  time = timeit.default_timer() - startTime
  print("== THE END ==")
  txt_out_info.write('Time = %f for 1 frame\n' % (time))
  print('Time : ', time) 
