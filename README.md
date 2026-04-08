# 📊 Marketing Attribution & Campaign Performance Analysis

---

## 🔍 Overview

This project combines **Python-based data processing and attribution modeling** with **Power BI-based business intelligence (BI) analysis** to evaluate how different marketing channels contribute to conversions and campaign performance.

Since the dataset did not contain sequential customer journey data, **customer journeys were simulated** to enable attribution modeling.

👉 The project answers:
**“Which marketing channels drive conversions, and how does attribution model choice affect decision-making?”**

---

## 📁 Dataset

* Source: Digital Marketing Campaign Dataset
* Type: Campaign-level data (transformed into journey-level data)

### Key Features:

* CustomerID
* CampaignChannel (Email, PPC, SEO, Social Media, Referral)
* AdSpend
* ClickThroughRate
* ConversionRate
* WebsiteVisits, PagesPerVisit, TimeOnSite
* EmailOpens, EmailClicks

---

## 🛠️ Data Processing

### 🔹 Conversion Engineering

Since the dataset did not include a binary conversion label:

```
Conversion = IF(ConversionRate > 0.15, 1, 0)
```

---

### 🔹 Customer Journey Simulation

To enable attribution modeling:

* Multiple touchpoints were generated per customer
* Marketing channels were assigned across interactions
* Final interaction marked as conversion

---

## 🐍 Python Analysis

Python was used for:

* Data cleaning and preprocessing
* Conversion feature engineering
* Customer journey simulation
* Attribution model implementation:

  * First-Touch Attribution
  * Last-Touch Attribution
  * Multi-Touch (Linear Attribution)

👉 This transformed campaign-level data into a **customer journey dataset suitable for attribution analysis**.

---

## ⚙️ Attribution Models Used

### 1. First-Touch Attribution

Credits the **first interaction**, identifying awareness channels

### 2. Last-Touch Attribution

Credits the **final interaction**, identifying conversion drivers

### 3. Multi-Touch (Linear Attribution)

Distributes credit equally across all touchpoints

---

## 📊 Attribution Results

| Channel  | First Touch | Last Touch | Multi Touch |
| -------- | ----------- | ---------- | ----------- |
| Email    | 1611        | 1616       | 1604        |
| PPC      | 1568        | 1626       | 1601        |
| Referral | 1608        | 1572       | 1585        |
| SEO      | 1618        | 1601       | 1612        |

---

## 📈 Power BI Dashboard

An interactive dashboard was built using **Power BI** to visualize attribution results and campaign performance.

---

### 🖼️ Dashboard Preview

![Dashboard](Dashboard.png)

---

## 📊 Key Visuals

### 🔹 Attribution Model Comparison

* Compares First-Touch, Last-Touch, and Multi-Touch models
* Highlights differences in perceived channel importance

---

### 🔹 Conversion Rate by Channel

* Shows average conversion performance across channels

---

### 🔹 Email Engagement Analysis

* Compares Email Opens vs Email Clicks
* Segmented by conversion outcome

---

### 🔹 User Behavior vs Conversion

* Website Visits
* Pages Per Visit
* Time on Site

👉 Identifies behavioral patterns of converting users

---

### 🔹 Scatter Plot Analysis

* Ad Spend vs Conversion Rate
* Bubble size represents Click Through Rate

👉 Reveals efficiency of marketing spend

---

## 💡 Key Insights

### 🔥 Attribution Insights

* **PPC dominates last-touch attribution**, indicating strong closing capability
* **SEO leads first-touch attribution**, highlighting its role in customer acquisition
* **Email performs consistently across models**, contributing across the funnel
* Multi-touch shows **balanced contribution across channels**

---

### 📊 Business Intelligence Insights

* Higher user engagement (time, pages) leads to higher conversion probability
* **Email clicks are more impactful than email opens**
* High ad spend does **not always translate into high conversion rates**
* Channel performance is relatively balanced across campaigns

---

### ⚠️ Important Observation

Different attribution models produce different results:

> Relying only on last-touch attribution may misrepresent the true contribution of awareness channels like SEO.

---

## 🚀 Conclusion

This project demonstrates how combining:

* Python-based data transformation
* Attribution modeling
* Business intelligence visualization

provides a **holistic understanding of marketing performance**.

👉 Multi-touch attribution is recommended for better decision-making.

---

## 🛠️ Tools Used

* Python (Pandas, NumPy)
* Power BI
* GitHub

---

## 📂 Project Structure

```
marketing-attribution-analysis/
│── digital_marketing_campaign_dataset.csv
│── attribution_results.csv
│── analysis.py
│── Dashboard.png
│── README.md
```

---

## 📌 Future Improvements

* Implement **Markov Chain Attribution Models**
* Use real-world sequential customer journey datasets
* Deploy as an interactive web dashboard

---

## 🙌 Author

**Sarika Kothapalli**
Aspiring Data Analyst | Passionate about Data, Business & Storytelling

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to connect!
