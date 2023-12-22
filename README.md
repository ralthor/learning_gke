# Local using Docker

## Build and Start

```
docker build -t my_flask_app .
docker run -p 5000:80 --name flask_app my_flask_app
```

## Stop and Remove

```
docker stop flask_app
docker rm flask_app
```

# GKE Commands

I ran it in Windows 11 powershell.

This is needed to allow script execution in PowerShell temporarily:

```
Set-ExecutionPolicy Bypass -Scope Process
```

Create the image in google cloud repository

```powershell
gcloud builds submit --tag gcr.io/<gc project name>/first .
```

Create the container cluster

```powershell
gcloud container clusters create my-1st-cluster --num-nodes 1 --issue-client-certificate --zone us-east1
```

It was successful, but also asked me to install the auth-plugin. I did:

```
gcloud components install gke-gcloud-auth-plugin
```

Finally, deploy to gke:

```
kubectl apply -f deployment.yaml
```

## Deleting the resources

```
kubectl delete deployment --all -n your-namespace
kubectl delete service --all -n your-namespace
gcloud container clusters delete your-cluster-name --zone your-zone
```
