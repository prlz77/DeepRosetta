
if !type "$wget" > /dev/null; then
	echo "Please, install wget tool"
	echo "If you are working with Debian, I suggest: sudo apt-get update && sudo apt-get install wget"
	exit 1
fi
wget http://www.vlfeat.org/matconvnet/models/imagenet-vgg-s.mat

