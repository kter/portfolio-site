docker build -t portfolio-site/css_generator .
docker tag portfolio-site/css_generator:latest 848738341109.dkr.ecr.ap-northeast-1.amazonaws.com/portfolio-site/css_generator:latest
docker push 848738341109.dkr.ecr.ap-northeast-1.amazonaws.com/portfolio-site/css_generator:latest
docker run -e BUCKET_NAME=kter.jp portfolio-site/css_generator