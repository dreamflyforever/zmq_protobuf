## profile   
This is the project for test python zmq protobuf.

## test
product proto file  
protoc --proto_path=. --python_out=. test_protobuf.proto  

run 'python ./zmqsub.py' & 'python ./zmqpub.py'  

## license
MIT by Jim

## maybe problem
pip install protobuf==3.20.3
