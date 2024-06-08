
# Operational report

- Cluster **productiondemo** (clus:PMx9HGEG_ZE)
- Reporting period:
    - Start: 2024-05-06 13:40:01
    - End: 2024-05-06 14:06:41

## 1. Cluster summary metrics

| Metric         | Value            |
|:---------------|:-----------------| 
| Number of nodes| 3 | 
| Number of namespaces| 8 | 
| Number of pods| 39 | 
| Number of deployments| 9 | 
| Number of daemonsets| 4 | 
| Number of services| 55 | 


## 2. Node information

| Node property | Value | Node count |
|:--------------|:------|:-----------| 
|  Instance Type| m5.large | (3/3) nodes | 
|  Nr of cores| 2 | (3/3) nodes | 
|  Hardware Arch| amd64 | (3/3) nodes | 
|  OS| Amazon Linux 2 | (3/3) nodes | 
|  Container Runtime| containerd://1.7.11 | (3/3) nodes | 


## 3. Node capacity and headroom

### Pods headroom

No nodes found with headroom capacity issues for number of pods



### CPU headroom

No nodes found with cpu headroom capacity issues



### Memory headroom

No nodes found with memory headroom capacity issues


---
## 4. Spyderbat agent health

### Spyderbat Nano-agent
> The spyderbat nano-agent runs as a daemonset on all nodes and monitor for system level telemetry on the host,
> using EBPF technology. It provides information on processes, networking and container runtime behavior.


✅ nano agent is running on all nodes





### Spyderbat Cluster Monitor
> The spyderbat cluster monitor runs as a deployment on the cluster, and monitors the kubernetes cluster
> lifecycle by talking to the kubernetes api. It provides information on current state of the cluster.


✅ cluster monitor is running


---
## 6. Cluster operational issues


No operational issues found



