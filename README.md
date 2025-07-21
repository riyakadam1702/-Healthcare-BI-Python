#  HealthCare Dashboard

---

## Overview

Hospitals face growing pressure to manage increasing patient loads, optimize bed utilization, allocate limited resources, and ensure quality care across departments. However, without a clear, data-driven understanding of operational and patient-level trends, decision-making remains reactive and fragmented.

This project addresses inefficient hospital resource allocation and patient care planning by building a robust analytical solution using **Power BI** for interactive dashboards and **Python** for data exploration and preprocessing. The goal is to provide a holistic view of hospital and patient operations, identify gaps, and suggest actionable strategies for improved healthcare delivery.

---

##  Data Description

###  Hospital Data

- **Hospital_code** – Unique identifier assigned to each hospital  
- **Hospital_type_code** – Type/category of the hospital (e.g., A, B, C)  
- **City_Code_Hospital** – Code representing the city where the hospital is located  
- **Hospital_region_code** – Region in which the hospital is situated (e.g., X, Y, Z)  
- **Available Extra Rooms in Hospital** – Number of extra rooms currently available  
- **Department** – Department where the patient was treated (e.g., Radiotherapy, Anesthesia)  
- **Ward_Type** – Type of ward (e.g., R, S, Q)  
- **Ward_Facility_Code** – Code for facilities provided in the ward  
- **Bed Grade** – Quality rating of the bed (e.g., 1.0, 2.0)

###  Patient Data

- **case_id** – Unique ID for each patient visit  
- **patientid** – Unique identifier for each patient  
- **City_Code_Patient** – Code representing the patient's city  
- **Type of Admission** – Reason for admission (e.g., Emergency, Trauma, Urgent)  
- **Severity of Illness** – Level of illness (Mild, Moderate, Extreme)  
- **Visitors with Patient** – Number of visitors accompanying the patient  
- **Age** – Age group (e.g., 0-10, 41-50)  
- **Admission_Deposit** – Deposit amount paid upon admission  
- **Stay** – Duration of stay (e.g., 0-10 days)

---

##  Insights & Suggestions

### 1 Strategic Capacity Building in Hospital Types ‘A’ and ‘B’

**Insight:**  
Hospital Types ‘A’ and ‘B’ manage the highest patient load and have the most extra rooms available, indicating better infrastructure readiness. Lower-tier hospitals like ‘F’ and ‘G’ show limited patient volume and facilities.

**Suggestion:**  
Invest in advanced medical facilities and specialist staff in Types ‘A’ and ‘B’ in Region 'X'. Use these as referral hubs for complex cases from under-equipped hospitals to enhance care quality and efficiency.

---

### 2 Bed Grade in Surgery Department

**Insight:**  
The Surgery department has one of the lowest average bed grades despite its critical role.

**Suggestion:**  
Upgrade bed quality and infrastructure in Surgery to support better post-operative recovery and reduce risks.

---

### 3 Admission Deposit Policy

**Insight:**  
Total deposits exceed ₹2 billion, averaging ~₹5K per patient—suggesting a uniform deposit system across admission types.

**Suggestion:**  
Revisit deposit structures to reflect admission severity. Consider deferred or insurance-based models for urgent cases. Offer financial support schemes for elderly patients (70+).

---

### 4 Patient Segmentation & Engagement

**Insight:**  
Age groups 41–60 dominate patient demographics.

**Suggestion:**  
Roll out mid-life wellness programs (e.g., diabetes, heart screenings) and loyalty/digital tracking apps to improve patient retention and health outcomes.

---

### 5 Capacity Planning & Resource Allocation

**Insight:**  
Moderate severity cases dominate with 175.84K patients.

**Suggestion:**  
Strategically allocate beds and specialists to this group while maintaining contingency for extreme cases. Use predictive modeling to plan resources based on seasonal severity patterns.

---

