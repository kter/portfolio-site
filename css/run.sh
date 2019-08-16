docker build -t portfolio-site/css_generator .
docker run -v $PWD:/app portfolio-site/css_generator
