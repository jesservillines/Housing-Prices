### Contents:
- [Problem Statement](##Problem-Statement)
- [Executive Summary](#Executive-Summary)
- [Data Dictionary](##Data-Dictionary)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)



## Problem Statement

The state of California is responsible for allocating 58% of the $97.2 billion dollars of 2018-19 funding for California's public schools ([source](https://www.ppic.org/publication/financing-californias-public-schools/)). This project aims to provide guidance for the State of California's Education Budget and make recomendations on the best way to track student success. California performs worse than the national average in the SAT and wants to improve student performance. This study examines local factors of sub-benchmark standardized test scores for students. The state wants to examine the nationally administered ACT and SAT in addition to the state administered CAASSP (California Assessment of Student Performance). As colleges trend away from using the ACT/SAT ([source](https://www.washingtonpost.com/education/2019/10/18/record-number-colleges-drop-satact-admissions-requirement-amid-growing-disenchantment-with-standardized-tests/)) California wants to make sure that they have viable ways to measure student outcomes. The goal is to optimize the effectiveness of each dollar of education spending by the state.


# Executive Summary

In pursuit of this goal, the state wants to identify barriers to a student's academic preparation for higher education. The scope of this analysis is to briefly compare California's ACT/SAT results to the nation's and compare national standardized college readiness tests to the state administered CAASSP as viable measures of student outcomes. Then it examines the relationship of college readiness in California's counties in order to provide a summary of possible causes for poor performance and make suggestions for improvement. 

I begin by comparing California's ACT/SAT test results to the nation's ACT/SAT test results. Here we find that the state of California is doing a mixed job compared to the national average in preparing our students for college entrance exams depending on the test.  

|Description|Scope|Average|Standard Deviation|Summary|
|---|---|---|---|---|
|ACT|USA|21.5|2.1|95% of students score between 19.4 and 23.5|
|SAT|USA|1120|90|95% of students score between 1030 and 1210|
|ACT|CA|22.6|+0.5 deviations from national mean|score is 1.1 points higher than national average|
|SAT|CA|1065|-0.5 deviations from national mean|score is 45 points lower than national average|

For the ACT our students, on average, score half a standard deviation above the mean. For the SAT, our students score one standard deviation below the mean. In addition, there is a mix of preference in picking the ACT or SAT across districts and schools in California, but this preference favors the SAT. Performance in this test is an area for improvement. 

|Rates of CA Participation|
|---|

|Year|ACT|SAT|
|---|---|---|
|2017|31%|53%|
|2018|27%|60%|
|2019|23%|63%|

Given the provided California SAT/ACT data sets there is no way to tell if a student took both the ACT and SAT, only the rates at which a student is taking either test. In order to avoid counting a student who took both the ACT and SAT, I filtered the data set to include only the scores for the test that was most taken in each county and district. I also removed records that were empty (schools that did not take the test in question) and schools with anonymous records (less than 15 tests taken). I also focused on only 11th grade students from the CAASSP dataset. What this project measures is the percentage of students in a county that did not meet benchmark scores in either test. A benchmark score is a score that when met or exceeded is deemed acceptable for college readiness. Here are the benchmark scores for the ACT/SAT/CAASSP.  

|Benchmark Scores for the ACT/SAT|
|---|

|Test|Benchmark Score|---|
|---|---|---|
|ACT|21 or higher|[source](https://www.cde.ca.gov/ds/sp/ai/reclayoutact19.asp)|
|SAT|1020 or higher|[source](https://www.cde.ca.gov/ds/sp/ai/glossarysat2019.asp)|
|CAASSP|State Determined|---|

The ACT measures a students performance in the following subjects: English, mathematics, reading and science ([source](http://www.act.org/content/act/en/products-and-services/the-act-educator/the-act-test.html#order-reg-materials)). The SAT test is split into two sections, Math and Evidence-based Reading and Writing ([source](https://www.princetonreview.com/college/sat-information)) These tests are used by college admission departments in deteriming acceptance and financial aid for a student at their respective school. Look here for more information about the [ACT](https://www.act.org/content/act/en.html) and here for more information about the [SAT](https://collegereadiness.collegeboard.org/sat). 

In addition to the nationally administered ACT and SAT, I look at the state administered California Assessment of Student Performance and Progression ([CAASSP](https://www.caaspp.org/faqs/all-faqs.html)) test. Similar to the ACT/SAT the CAASSP measures a student's performance in the academic catagories of English, math and science. Since CAASSP scores are administered for grades 4-8 and 11th grade they could be useful as an early indicator of a students track towards college prepardness since it is administered more frequently and at younger ages ([source](https://www.cde.ca.gov/ta/tg/ca/caasppkeypts.asp#:~:text=Because%20CAASPP%20tests%20are%20given,to%20improve%20teaching%20and%20learning)). This is an area for additional research.

The geographic distribution of benchmark scores is similar for both the national tests and the state test suggesting that there are specific local factors that influence test scores:

![](/data/cali_map.png)


This study then examined the distribution of median household income and poverty rate under 18 throughout the state and found that these measures of income inequality trend with standardized academic test results. There is a strong correlation between socio-economic factors and standerdized test results. This study does not examine causality, but suggests this as an area for additional research.  

![](/data/youthpoverty_actsat_scatter.png)

I take a look at a combination of national and state specific data.


## Data Sets used
| Data File Name | Link to Data Source |Description| Scope|
|---|---|---|---|
| sat_2019_ca.csv | [source](https://www.cde.ca.gov/ds/sp/ai/glossaryact2019.asp) | For SAT benchmark scores by county | California|
act_2019_ca.csv |[source](https://www.cde.ca.gov/ds/sp/ai/glossarysat2019.asp) | For ACT benchmark scores by county| California|
act_2017.csv |[source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)| Average ACT Scores by State, 2017| USA|
act_2018.csv |[source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows) | Average ACT Scores by State, 2018| USA|
act_2019.csv |[source](https://www.cde.ca.gov/ds/sp/ai/) | Average ACT Scores by State, 2019| USA|
sat_2017.csv |[source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/) | Average SAT Scores by State, 2017| USA|
sat_2018.csv |[source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/) | Average SAT Scores by State, 2018| USA|
sat_2019.csv |[source](https://www.cde.ca.gov/ds/sp/ai/) | Average SAT Scores by State, 2019| USA|
caassp00.txt through caassp07.txt |[source](https://caaspp-elpac.cde.ca.gov/caaspp/ResearchFileList?ps=true&lstTestYear=2019&lstTestType=B&lstGroup=1&lstGrade=13&lstSchoolType=A&lstCounty=01&lstDistrict=00000&lstSchool=0000000#dl) | CAASSP Results for all students 2018/2019| California|
|sb_ca2019entities_csv.txt|[source](https://caaspp-elpac.cde.ca.gov/caaspp/ResearchFileList?ps=true&lstTestYear=2019&lstTestType=B&lstGroup=1&lstGrade=13&lstSchoolType=A&lstCounty=01&lstDistrict=00000&lstSchool=0000000#dl)|Data Dictionary for CAASSP Results for all students|California|
|all-geocodes-v2016.xlsx|[source](https://www.census.gov/geographies/reference-files/2016/demo/popest/2016-fips.html)|2016 FIPS Codes from the Census for cholopeth maps|USA|
|development.csv|[source](https://www.labormarketinfo.edd.ca.gov/Population_and_Census.html)|Employment Development Dept. Population and Census data for local factors|California|

## Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|participation_sat|object|National ACT/SAT (act_sat.csv)|Participation rate in the SAT as a percent|
|state|object|National ACT/SAT (act_sat.csv)|Record State|
|total_sat_score|int|National ACT/SAT (act_sat.csv)|Total average SAT score for record state|
|year|object|National ACT/SAT (act_sat.csv)|Year record was created|
|participation_act|float|National ACT/SAT (act_sat.csv)|Participation rate in the ACT as a percent|
|total_act_score|float|National ACT/SAT (act_sat.csv)|Total average ACT score for record state|
|students_12th_grade|float|California ACT/SAT (cali.csv)|Number of students in 12th grade in schools participating in the ACT/SAT| 
|preferred_test_name|object|California ACT/SAT (cali.csv)|District/County preference in college admission test (ACT or SAT)| 
|preferred_test_num_taken|float|California ACT/SAT (cali.csv)|Number of students in 12th grade in schools participating in the ACT/SAT| 
|num_test_benchmark|float|California ACT/SAT (cali.csv)|Number of students that meet benchmark scores in the SAT or ACT| 
|prct_test_benchmark|float|California ACT/SAT (cali.csv)|Percentage of students that meet benchmark scores in the SAT or ACT| 
|cds|float|California ACT/SAT (cali.csv)|County/District/School Code| 
|cname|object|California ACT/SAT (cali.csv)|County name|
|dname|object|California ACT/SAT (cali.csv)|District name|
|year|object|California ACT/SAT (cali.csv)|Record year|
|county_code|float|CAASSP (casspp.csv)|CAASSP county code|
|county_name|object|CAASSP (casspp.csv)|california county name|
|students_with_scores|float|CAASSP (casspp.csv)|student's with CAASSP scores|
|percentage_standard_not_met|float|CAASSP (casspp.csv)|Percentage of students who did not meet the standard|
|percentage_standard_nearly_met|float|CAASSP (casspp.csv)|Percentage of students who nearly met the standard|
|percentage_standard_met|float|CAASSP (casspp.csv)|Percentage of students who meet the standard|
|percentage_standard_met_and_above|float|CAASSP (casspp.csv)|Percentage of students who met and passed the standard|
|percentage_standard_exceeded|float|CAASSP (casspp.csv)|Percentage of students who exceeded the standard|
|cali_county_fips|object|Census Geocodes|FIPS Geocode information for choropeth mapping|
|county|object|State Development data (development.csv)|County|
|population|object|State Development data (development.csv)|Population by county|
|proportion_pop_to_farmland|object|State Development data (development.csv)|Planted acres/population|
|poverty_under18_sum|object|State Development data (development.csv)|Poverty Rate, Under 18 as a percent|
|poverty_under18_percent|float|State Development data (development.csv)|Poverty Rate, Under 18 as a sum|
|hh_income|int|State Development data (development.csv)|Median Household Income 2016| 




# Conclusions and Recommendations

Conclusion:

There is a link between local factors and student outcomes on standardized academic assessments. When allocating state funds to school districts these local factors need to be considered. Student outcomes are a local problem and need local solutions. 

The distribution of sub-benchmark students differs widely based on county. Counties with the highest rates of sub-benchmark students were sub-benchmark for all examined assessment tests. This suggests that national and state academic assessment tests favor and disfavor the same bins of students. I then examined the bins of sub-benchmark students for shared local factors. This local analysis shows a strong link between median household income, poverty rates under the age of 18, and a student's result on academic assessment tests. If median household income is lower than average in a county, test results are more likely to be sub-benchmark. If rates of rates of poverty under 18 years of age are higher, test results are more likely to be sub-benchmark. 


Recommendations:

1)  Allocate more funds to districts with median household income that are lower than the average household median income for California. Particularly the districts in the counties of Del Norte, Tehama, Merced, and Modoc.
Specific recomendations to help level the playing field for lower household income/higher poverty rate areas:
* Provide schools with nutritional free lunches. Access to healthy food can improve academic performance. [source](https://www.brookings.edu/blog/brown-center-chalkboard/2017/05/03/how-the-quality-of-school-lunch-affects-students-academic-performance/#:~:text=We%20find%20that%20in%20years,(about%204%20percentile%20points).)
* Update computer labs for lower income areas where there may not be available computers at home.
* Create scalable software academic assessment test tutoring solutions.
* Look at the CAASSP instead of the ACT/SAT as a measure of student benchmark prepardness.

2) Examine additional characteristics within these counties to look for more determinant of student academic outcomes. A more complete model would be helpful in removing barriers for adversely affected students. 

Suggestions for continued analysis include: 

* English Learners per capita. A non-native English speaker may have additional trouble on the English portions of academic assessment tests. If there are more English learners language tutors could a netter use of educational funds than academic tutoring software.

* Crime rates per capita. High crime rates in home neighborhoods could distract students from studying. Providing healthy outlets such as additional after school programs or library study hours could be helpful. 

* Student Drop-out Rates.   

* Farmed acres per capita (California is major agricultural producer ([source](https://www.cdfa.ca.gov/Statistics/#:~:text=Over%20a%20third%20of%20the,the%20nation's%20total%20agricultural%20value.)). Are the counties more agricultural? If so, can we design class projects around harvest schedules when students may be assisting parents with harvest)

