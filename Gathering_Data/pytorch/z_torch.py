import torch; print(torch.__version__)

if torch.cuda.is_available():
    print ("gpu is avaialabale")
    print(f"using gpu: {torch.cuda.get_device_name(0)}")
else:
    print("gpu is not available")