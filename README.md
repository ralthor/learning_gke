# GKE Commands

I ran it in Windows 11 powershell.

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

Finally, deployed to gke:

```
kubectl apply -f deployment.yaml
```
