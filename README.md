#  S.Dash – Sugar Data Dashboards (Capstone Project 3)

##  Project Overview
This project contains two interactive web dashboards built using **Flask**, **SQL**, and **Chart.js**, based on a global sugar consumption dataset.
---

##  Objectives

- Create two interactive dashboards using the cleaned dataset from Capstone Project 2
- Integrate front-end and back-end (Flask + SQL + JavaScript)
- Present meaningful data stories with visualizations
- Ensure excellent user experience (UX) and design

---

##  Dashboards

### 1️ **Sugar & Health Risk Dashboard** (Analytical)
- **Audience**: Health experts, NGOs, researchers
- **Goal**: Identify countries and regions at risk of sugar-related diseases
- **Key Features**:
  - Context cards with global average sugar intake, obesity, and diabetes rates
  - Visual analysis of risk patterns and sugar composition
  - Interactive filters and deep-dive data

####  Quantitative Charts:
1. **Scatter Plot** – Sugar Intake vs Diabetes Prevalence  
   Shows the correlation between two numerical health indicators per country.

2. **Bar or Lollipop Chart** – Top 10 Countries by Avg Daily Sugar Intake  
   Highlights countries with the highest average daily sugar consumption.

####  Qualitative Charts:
3. **Pie Chart** – Sugar Source Composition  
   - **Why**: Pie charts emphasize categorical part-to-whole relationships.  
   - **Categories**: `sugar_from_sugarcane`, `sugar_from_beet`, `sugar_from_HFCS`, `sugar_from_other`  
   - **How it’s Qualitative**: Focus is on the distribution of sugar types, not precise quantities.

4. **Segmented Horizontal Bar Chart** – Health Risk Profile by Region  
   - **Type**: Qualitative  
   - **Visual**: Horizontal bar per region with 2 segments:
     - Segment 1: Average obesity rate  
     - Segment 2: Average diabetes prevalence  
   - **How it’s Qualitative**: Focuses on regional patterns and composition of health risk.

---

### 2️ **Sugar Policy & Trade Dashboard** (Strategic)
- **Audience**: Government policymakers, economists
- **Goal**: Understand how sugar import/export and taxation relate to public health and the economy
- **Key Features**:
  - Trade comparisons by region
  - Tax visualization across countries
  - Economic-health analysis tools

#### Charts:
- **Scatter Plot with Bubble Size** – GDP vs Sugar Tax per Capita (bubble = obesity)
- **Curved Line/Area Chart** – Sugar Import vs Export by Region
- **Choropleth Map** – Tax per Capita by Country
- **Data Table** – Top Sugar Producing Countries

