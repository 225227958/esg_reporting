# ESG Reporting Analysis
Environmental, Social, and Governance (ESG) disclosures are designed to measure a corporation’s resilience to ESG risks, its impact on society, the environment and their internal governance. Conceptually, ESG disclosures bridge the gap between traditional financial reporting and non-financial performance. There are three main pillars used to measure their performance:
•	Environmental (E) – This pillar has in focus how a company takes care of the natural environment. Key metrics for this case include Greenhouse Gas emissions, water consumption, waste generation, and impacts on biodiversity and land use.
•	Social (S) – The Social pillar measures a company’s relationship with its workforce, suppliers, and customers. Key metrics include labor practices, workplace health and safety, employee turnover, equity, diversity, inclusion metrics, human rights compliance, etc.
•	Governance (G) – Measures the internal system of practices, controls and procedures a company uses to govern itself, make decisions and comply with the law. Key metrics include anti-bribery and corruption controls, tax transparency, shareholder rights, board composition (diversity, independence), etc.

The analysis focuses on four companies from different industries:

ExxonMobil (Oil & Gas)
RWE (Utilities)
Hugo Boss (Fashion)
LVMH (Luxury Goods)

Using DataNXT, ESG reports are generated from company documents, governance materials, financial reports, and external sources. Official ESG reports are intentionally excluded from the generation process and are used only for benchmarking.

# Research Motivation
ESG reporting has become one of the main tools companies use to communicate their environmental, social, and governance performance.
However, ESG disclosures often face challenges such as:

Greenwashing and selective disclosure
Lack of standardization across reporting frameworks
Limited external assurance
Inconsistent reporting boundaries
Difficulties in comparing companies and industries

# Research Hypotheses:
This project is based on three main assumptions:
H1 – Standardization
Companies following recognized reporting standards (ISSB, CSRD, GRI) are expected to produce more comparable and useful ESG disclosures.
H2 – Materiality
High-quality ESG reports focus on the most material sustainability topics affecting the company and its stakeholders.
H3 – Governance Integration
Meaningful ESG reporting demonstrates that sustainability is embedded within corporate decision-making processes rather than being used solely as a communication tool.

# Data Collection
For each company, documents were collected from five categories:
Company
│
├── Environmental
├── Social
├── Governance
├── Financial
├── External

Input Sources:
Environmental policies and climate documents
Social and human rights policies
Governance documentation
Financial reports and investor presentations
External sources such as news articles and stakeholder reports

Official ESG and sustainability reports were excluded from the AI workflow and stored separately in the Comparison folder. These reports were used only during the final evaluation stage.
Baseline Workflow Development
Although all four companies are included in the analysis, LVMH was used as the initial company for workflow development.
LVMH provides substantial coverage across all three ESG pillars:

Environmental (climate, biodiversity, LIFE 360)
Social (human rights, labour practices, supply-chain management)
Governance (executive compensation, ethics, board oversight)

This made it possible to test the workflow against a broad range of ESG topics before applying the same methodology to ExxonMobil, RWE, and Hugo Boss.
Note: To complement the classical text analysis, an LLM-based analysis was conducted focusing on factual consistency, completeness, specificity, and framing. Initially, this analysis was planned as part of the Python workflow. However, API access was limited by quota restrictions, and running local models through Ollama significantly affected system performance. Therefore, the LLM analysis was carried out manually using a structured prompt and the same evaluation criteria for each company.
# Classical Text Analysis
Length and Coverage
A noticeable difference emerged when comparing the size of the reports. For LVMH, ExxonMobil, and RWE, the AI-generated reports were considerably shorter than the official ESG reports. While the generated reports covered the main sustainability themes, they often condensed information that was discussed in much greater depth in the corporate disclosures. Hugo Boss was the only exception, with the generated report containing more text than the official sustainability report.

Similarity Analysis
To understand how closely the generated reports resembled the official ones, TF-IDF Cosine Similarity and Jaccard Similarity were calculated. Across all four companies, the similarity scores were moderate rather than high. This suggests that the AI generally identified the same ESG topics as the official reports, but often presented them differently, both in terms of wording and structure.
ExxonMobil achieved the highest similarity scores, indicating the strongest alignment between the generated and official report. In contrast, Hugo Boss and RWE displayed lower similarity values, pointing to larger differences in content emphasis and report composition.

ESG Vocabulary and Disclosures
The keyword analysis highlighted an interesting pattern. References to ESG-specific concepts such as Scope 3, Materiality, and TCFD appeared much more frequently in the official reports. This is not particularly surprising, as official sustainability reports are designed to satisfy reporting standards and regulatory requirements. The generated reports, on the other hand, tended to describe sustainability performance in broader and more general terms instead of explicitly referencing reporting frameworks.

ESG Topic Coverage
When looking at ESG topic distribution, environmental content occupied a larger share of the generated reports than it did in several of the official reports. This trend was especially visible for ExxonMobil and RWE, where climate change, emissions, and energy transition issues dominate much of the sustainability discussion.
Coverage of social and governance topics was still present, but the balance between the three ESG pillars often differed. In some cases, the generated reports placed greater attention on environmental challenges, while the official reports allocated more space to governance structures, compliance mechanisms, or social initiatives.

Sentiment Analysis
Both the generated and official reports generally conveyed a positive tone. This was expected, given that sustainability reporting often focuses on achievements, targets, and progress made toward ESG objectives.
The topic-specific results showed a similar pattern across environmental, social, and governance themes. However, the AI-generated reports were usually slightly more positive, particularly when discussing environmental performance. This could indicate that the generated reports place stronger emphasis on achievements and future ambitions, whereas official reports are somewhat more balanced in discussing progress, risks, and remaining challenges.

# LLM Analysis - LVMH 
Factual Consistency
The generated report identified most of the same ESG topics that appear in the official report. Climate change, biodiversity, responsible sourcing, human rights, and governance were all discussed in both documents. The report also correctly recognized the importance of LVMH's LIFE 360 strategy and its focus on environmental improvement across the value chain.
At the same time, the generated report relied more heavily on publicly available information and external sources, which sometimes resulted in broader conclusions than those found in the official report.
Completeness
The generated report covered the majority of LVMH's key ESG themes, but not necessarily with the same emphasis. While the official report spent considerable time describing environmental programs, employee initiatives, and governance structures, the generated report concentrated more on the issues it considered most material to the company.
As a result, the generated report provided a focused ESG assessment, whereas the official report presented a broader picture of the company's sustainability activities.
Specificity
A noticeable difference was the type of information presented. The official report relied heavily on KPIs, progress updates, and examples from individual business segments. The generated report included some figures and targets but focused more on explaining ESG issues and their significance to the company.
The generated report therefore felt more analytical, while the official report felt more operational and performance-oriented.
Framing
This was the biggest difference between the two reports.
The official report presented LVMH primarily through its sustainability programs, achievements, and long-term commitments. Biodiversity initiatives, sourcing programs, and environmental targets were generally described from the perspective of progress and improvement.
The generated report looked at the company from a different angle. Alongside achievements, it paid much more attention to potential risks surrounding supply-chain transparency, sourcing practices, and human-rights concerns. These subjects were still present in the official report, but they played a much larger role in the generated assessment.
Because of this, the two reports often discussed the same ESG topics but told slightly different stories about them.
# LLM Analysis - Hugo Boss
Factual Consistency
Both reports focused heavily on sustainable sourcing, human rights, circularity, emissions reduction, and supplier management. Since Hugo Boss relies on a large global supplier network, the generated report also correctly identified the supply chain as one of the company's most important ESG challenges.
Overall, no major contradictions between the two reports. Most of the key sustainability priorities mentioned in the official report were also present in the generated version.
Completeness
The difference was mostly in what each report chose to focus on.
The official report spends a lot of time discussing sustainability targets, progress updates, and performance indicators. There are many statistics related to employee satisfaction, gender diversity, renewable energy, supplier compliance, and material sourcing. The generated report covered the same general topics but spent more time explaining sustainability risks and challenges rather than reporting progress against individual targets. Because of that, it felt more like an ESG assessment than a sustainability performance report. 
Specificity
The official report relies heavily on measurable targets and KPIs. Almost every major sustainability topic is supported by percentages, targets, or progress figures. 
The generated report was specific in a different way. Instead of focusing on performance metrics, it provided more context around sourcing risks, labour rights, supplier oversight, and ESG challenges within the fashion industry. This made the report easier to read, but less data-driven than the official report.
Framing
In the official report, the supply chain was mainly discussed through supplier standards, sustainability targets, and responsible sourcing initiatives. The overall message was that Hugo Boss has systems in place to manage these issues and is making progress toward its sustainability goals. 
The generated report looked at the same area from a different perspective. It spent much more time discussing labour-rights concerns, supplier-related risks, and sourcing controversies. Cases involving Xinjiang cotton and labour conditions in supplier factories received a level of attention that was largely missing from the official report.
This makes the generated report feel more focused on the risks behind the supply chain, while the official report focused more on the actions being taken to improve it.

# LLM Analysis RWE
Factual Consistency
The generated report was generally aligned with the official RWE ESG report. Both reports identified climate change, decarbonization, renewable energy expansion, and the energy transition as the company's most important ESG topics. The generated report also correctly highlighted RWE's net-zero ambition, large investments in renewable energy, and emissions reductions achieved through the phase-out of coal-fired generation.  RWE is presented as a company in transition, moving away from fossil fuels while rapidly expanding renewable energy capacity in both reports.
Completeness
The generated report covered most of the ESG issues that dominate RWE's sustainability profile. Topics such as renewable energy investments, emissions reductions, biodiversity, human rights, governance, and sustainable finance were all discussed. The official report, however, spent much more time explaining the scale of these activities through detailed operational information. It included extensive data on renewable generation capacity, electricity production, emissions, investments, governance committees, and financial performance. The generated report focused less on these operational details and more on explaining the sustainability implications behind them. 
Specificity
The generated report contained several important numbers and targets, such as emissions reductions, renewable energy growth, and net-zero commitments. This helped support many of the ESG claims being made. The official report was much more detailed and relied heavily on KPIs, generation statistics, investment figures, and performance metrics. While the generated report explained what RWE is doing, the official report provided much more evidence to show how those goals are being achieved and measured. 
Framing
The way the energy transition was presented was noticeably different between the two reports.
The official report focused strongly on progress. Renewable energy expansion, investments, emissions reductions, future growth plans, and financial performance were at the centre of the discussion. The overall message was that RWE is successfully executing its transition strategy. 
The generated report looked at the transition from a broader ESG perspective. Alongside the positive developments, it repeatedly highlighted the challenges that remain, including ongoing dependence on coal and lignite generation, climate-related litigation, and criticism from environmental stakeholders. These topics were discussed much more prominently than in the official report. As a result, the generated report felt more focused on the difficulties of the transition, while the official report focused on the progress being made.

# LLM Analysis ExxonMobil
Factual Consistency
The generated report aligned closely with the themes presented in ExxonMobil's official climate report. Both documents identified climate change, greenhouse gas emissions, methane reduction, carbon capture and storage (CCS), hydrogen, and governance oversight as central ESG topics. Both also recognized that ExxonMobil is attempting to reduce operational emissions while continuing to operate a large oil and gas business. The generated report correctly highlighted ExxonMobil's focus on methane reduction, CCS investments, lower-carbon technologies, and its net-zero ambition for operated Scope 1 and Scope 2 emissions.
Completeness
The two reports covered many of the same ESG issues, but they approached them with different levels of detail.
The official report devoted extensive attention to ExxonMobil's climate solutions portfolio, including CCS infrastructure, hydrogen technologies, lithium production, lower-emission fuels, methane monitoring systems, and research and development activities. Many pages were dedicated to explaining individual technologies, investment plans, and future growth opportunities.
The generated report discussed these initiatives as well but focused more on the broader ESG implications of the company's strategy. Rather than describing individual projects in depth, it concentrated on understanding whether ExxonMobil's actions were sufficient to address its most significant sustainability challengesSpecificity
The official report relied heavily on quantitative evidence. It presented detailed emissions data, methane intensity reductions, flaring reductions, investment commitments, and descriptions of large-scale CCS and hydrogen projects. The report frequently used KPIs and technical metrics to demonstrate progress.
The generated report included important figures and targets as well, such as methane reductions, emissions intensity improvements, and net-zero commitments. However, the emphasis was placed more on explaining the significance of these actions and the broader ESG challenges facing the company rather than documenting every performance indicator. 
Framing
The most noticeable difference was how ExxonMobil's transition strategy was presented.
The official report framed ExxonMobil primarily as a company helping to solve the challenge of providing reliable energy while reducing emissions. Much of the discussion focused on technology, innovation, investment, and future growth opportunities in areas such as CCS, hydrogen, lower-emission fuels, lithium, and advanced materials. The overall narrative emphasized progress and the company's ability to play a role in a lower-emission future.
The generated report examined the same topics from a broader ESG perspective. While it acknowledged ExxonMobil's emissions reductions and technology investments, it devoted significantly more attention to the limitations of the company's current approach. In particular, the exclusion of Scope 3 emissions from its net-zero ambition, the continued expansion of oil and gas operations, and ongoing climate-related criticism were discussed much more prominently than in the official report.As a result, the two reports often discussed the same facts but attached different levels of importance to them.

# RESULTS
Classical Text Analysis
Similarity Analysis
The cosine similarity analysis revealed varying degrees of alignment between the AI-generated reports and the official sustainability reports.
          Company          AI Report Length   Official Report Length   Cosine Similarity
          ExxonMobil       2677               35525                    54.6%
          LVMH             3802               53604                    49.6%
          RWE              3660               146496                   33.5%
          Hugo Boss        2531               1005                     26.6%

ExxonMobil achieved the highest similarity score (54.6%), indicating the strongest textual alignment between the generated and official reports. LVMH also demonstrated relatively high similarity (49.6%). Hugo Boss produced the lowest similarity score (26.6%), suggesting greater differences in report structure, language, and focus.
A notable observation is that the generated reports were generally much shorter than the official sustainability reports while still capturing many of the key ESG themes. This was particularly evident for RWE, whose official report contained over 146,000 words compared to only 3,660 words in the generated report.

ESG Coverage Analysis
Environmental Coverage
         Company      AI Coverage  Official Coverage  
         ExxonMobil   63.4%        40.3%     
         RWE          48.3%        12.5%
         Hugo Boss    44.2%        62.5%
         LVM          H32.4%       28.9%