1. abrir consola en este directorio
2. copiar: 
	ssh -i "Gdelt.pem" ubuntu@ec2-44-234-147-72.us-west-2.compute.amazonaws.com (esta direccion cambia, consultar en AWS)
3. 	cd gdelt-downloader
4. 	python3 s3upload.py
5. al terminar:
	exit