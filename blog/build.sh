docker build -t portfolio-site/blog_updater .
docker tag portfolio-site/blog_updater:latest 848738341109.dkr.ecr.ap-northeast-1.amazonaws.com/portfolio-site/blog_updater:latest
docker push 848738341109.dkr.ecr.ap-northeast-1.amazonaws.com/portfolio-site/blog_updater:latest


