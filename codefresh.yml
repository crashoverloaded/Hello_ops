version: '1.0'
steps:
  build_image:
    type: build
    description: Building the image...
    image-name: myuser/myservice
    tag: develop # ${{CF_BRANCH}}

  perform_tests:
    image: node:5
    working_directory: ${{main_clone}}
    description: Performing unit tests...
    commands:
      - npm install gulp -g 
      - npm install
      - gulp unit_test
