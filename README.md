# Custom Object Detection using YOLOv3
This repository shows simple steps to create
1. Custom object detection dataset. 
2. Train a yolov3 model on the custom dataset. 
3. Test the trained model on images and video feed. 

## Results

![This is an image](/Output_Images/Output_Test8.jpg)

![This is an image](/Output_Images/Output_Test4.jpg)

## How to create a custom object dataset
1. Google search the object.
2. Add [Image assistant Batch Image downloader](https://chrome.google.com/webstore/detail/imageassistant-batch-imag/dbjbempljhcmhlfpfacalomonjpalpko?hl=en) to chrome extension. 
3. Use the extension to download all the images.
4. Clean the dataset
  - Remove unwanted images
  - Run the [script](image_finder.py) to identify smaller resolution images.
  - Convert the images to a similar format.
5. Use [labelImg](https://github.com/tzutalin/labelImg) to annotate images. (Select yolo while annotating) 

## Train a yolov3 model on the custom dataset

1. Open Train_YoloV3.ipynb in google colab.
2. Follow the steps in the notebook to train the model in colab.
3. Use appropriate configuration steps.
4. Download the trained model.

## Test the trained model on images and video feed
1. Run yolo_object_detection.py to detect the custom object on an image.
2. Run yolo_object_video_detect.py to detect the custom object on an image.

## Acknowldegments 
1. Thanks to [tzutalin](https://github.com/tzutalin/labelImg) to make the object detection annotation process so simple.
2. Few youtube links that helped me understand the training process. 
- https://www.youtube.com/watch?v=10joRJt39Ns
- https://www.youtube.com/watch?v=_FNfRtXEbr4






