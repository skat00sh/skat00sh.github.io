---
title: "Curriculum Vitae"
date: 2025-11-24
draft: false
---

## Professional Experience

### Verses Inc. 
**Sr. ML Research Engineer - Contractor, Remote** | Dec 2023 - Present
{{< collapse summary="Details" >}}
- Designed and deployed an edge-ready 3D perception stack for reliable warehouse object detection and depth-aware navigation on Jetson-class hardware.
- Developed an YOLOv10n perception pipeline for warehouse-specific objects using a BlenderProc2-curated synthetic dataset, improving mAP from 0.15 to 0.62 at 640×640 and reducing the sim-to-real gap by retraining the synthetic-initialized model on cleaned, real warehouse data to reach 0.58 mAP
- Optimized the end-to-end detection stack (pre/post-processing + YOLOv10n inference) with TensorRT on Jetson Orin NX and desktop GPUs, achieving 26 ms latency at 640×640 for real-time edge deployment
- Integrated a DepthAnythingv2-based depth estimation module into the TensorRT perception pipeline, cutting depth latency from 1 s to 50 ms and delivering a combined depth + detection stack at 10 FPS (640×640) and 13 FPS (378×378) on Jetson Orin NX

{{/collapse}}

### Verses Global Bv 
**ML Tech Lead (Project: <a href="https://www.daiedge.eu/">dAIEdge</a>) - Contractor, Remote** | Dec 2023 - Present
{{< collapse summary="Details" >}}
- Led development of an Active Inference–based routing agent leveraging the perception pipeline to perform obstacle avoidance, optimizing the planning stack and reducing planning time from 7 minutes to 21 seconds
- Developed a PyMDP-based saccading agent using a Tapo security camera for active visual exploration, enabling person detection and tracking and later forming the basis of a peer-reviewed conference publication
- Designed and maintained a 3D simulation pipeline in NVIDIA Isaac Omniverse to develop and evaluate routing agents in realistic warehouse environments before real-world deployment
**Publication:** Towards smart and adaptive agents for active sensing on edge devices, **D. Vyas**, M. De Prado and T. Verbelen, HiPeac 2025 <a href="https://arxiv.org/abs/2501.06262">Link</a> 

{{< /collapse >}}

### Machine Learning Engineer 
**TerraLoupe GmbH - Munich, Germany** | Oct 2019 – Apr 2020
{{< collapse summary="Details" >}}
- My responsibility involved improving toolchains for deep learning experiments to enhance their reproducibility and
trackability.
- Sourced, Cleaned and Automated MLOps pipeline for large-scale aerial image segmentation dataset
- Integrated ML experimentation tracking using Sacred and Omniboard
- Experimented with Deeplab(Semantic Segmentation Model) migration from GPUs to TPUs
{{/collapse}}

### ADAS Engineer 
**KPIT Technologies GmbH - Munich, Germany** | Jan 2019 – Aug 2019
{{< collapse summary="Details" >}}
- My task was to create a Vehicle State Monitor that handles high-frequency data from multiple sensors on the car
• Developed a GUI dashboard that can process processes high-frequency data to monitor and visualise the real-time health
of vehicles
- Designed the testing module for the Test Driven Development(TDD) of the Vehicle State Monitor (VSM)
- Contributed to coding standards, code reviews, and source control management
{{/collapse}}

### Software Engineer 
**CNRS (XLIM Lab) - Poitiers, France** | Jan 2017 – Aug 2018
{{< collapse summary="Details" >}}
- My responsibility was to integrate and optimize an algorithm for a simulator that visualizes radio wave propagation.
- Optimized run-times by approx. 30% and streamlining system reliability
**Publication:** CupCarbon: A new platform for the design, simulation and 2D/3D visualization of radio propagation and interferences in IoT networks
{{/collapse}}

## Education

### M.Sc. Informatics 
**Technical University of Munich** | Focus: ML and CV | Oct 2019 – Aug 2023


### Bachelors of Technology in Computer Science
**The LNM Institue of Information Technology, B.Tech Computer Science** | Jul 2012 – Jun 2016



## Skills

{{< collapse summary="Languages" >}}
- Python 
- C++
- MATLAB
- Java
- bash 
{{/collapse}}
### Libraries
{{< collapse summary="Libraries" >}}
- PyTorch
- Tensorflow
- ROS2
- PyMDP
- Jax
- OpenCV
- Numpy/CuPy
{{/collapse}}
<!-- ## Certifications
- AWS Certified Solutions Architect
- Google Cloud Professional Developer 
{{/collapse}}

## Languages
- English (Bilingual)
- German (A2+ level)
- Hindi (Native)

<!-- ## Projects
- [Project 1](https://github.com/yourusername/project1): Brief description
- [Project 2](https://github.com/yourusername/project2): Brief description -->

## Contact
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/your-profile)
- GitHub: [Your Profile](https://github.com/skat00sh) 