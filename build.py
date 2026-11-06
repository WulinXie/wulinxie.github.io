"""Generate a dependency-free English academic homepage: python3 build.py."""
from pathlib import Path
from html import escape
ROOT = Path(__file__).parent

def bi(en, zh):
    return f'<span>{en}</span>'
def link(url, label, cls=''):
    return f'<a href="{escape(url,quote=True)}" class="{cls}"'+(' target="_blank" rel="noopener noreferrer"' if url.startswith('https:') else '')+f'>{label}</a>'
def section_title(n,en,zh,extra=''):
    return f'<div class="section-heading"><h2><span class="section-no">{n}</span>{bi(en,zh)}</h2>{extra}</div>'

papers=[
 dict(id='vi',image='VI-Bench',tags='multimodal',venue='NeurIPS 2026',role=('First author','第一作者'),title='VI-Bench: Benchmarking Prompt Inversion from AIGC Videos',authors='<strong>Wulin Xie</strong>, Rui Zhao, Kecen Li, Xiujin Liu, Bokang Zhang, Zheng Liu, Xinwen Hou, Chen Gong',en='Can a model recover the prompt behind a generated video? A closed-loop benchmark with 900 verified videos and 18 VLMs connects video understanding to generation control.',zh='模型能否从生成视频中恢复可执行的生成提示？通过 900 个验证视频、18 个 VLM 的闭环评测，连接视频理解与生成控制。',links=[('Paper','https://arxiv.org/abs/2609.08079'),('Code','https://github.com/aba122/VI-Bench'),('Dataset','https://huggingface.co/datasets/wulin222/VI-Bench')],selected=True),
 dict(id='unify',image='MME-Unify',tags='multimodal',venue='ICLR 2026',role=('Co-first author','共同第一作者'),title='MME-Unify: A Comprehensive Benchmark for Unified Multimodal Understanding and Generation Models',authors='<strong>Wulin Xie</strong>, Yi-Fan Zhang, Chaoyou Fu, Yang Shi, Bingyan Nie, Hongkai Chen, Zhang Zhang, Liang Wang, Tieniu Tan',en='Evaluating understanding and generation together: 4,104 examples across 30 subtasks reveal the gap between strong individual capabilities and truly unified multimodal reasoning.',zh='联合评估理解与生成：以 4,104 条样本、30 个子任务，揭示单项能力与统一多模态推理能力之间的差距。',links=[('Paper','https://arxiv.org/abs/2504.03641'),('Project','https://mme-unify.github.io/'),('Code','https://github.com/MME-Benchmarks/MME-Unify')],selected=True),
 dict(id='hawkeye',image='Q-Hawkeye',tags='rl multimodal',venue='AAAI 2027 · Under Review',role=('First author','第一作者'),title='Q-Hawkeye: Reliable Visual Policy Optimization for Image Quality Assessment',authors='<strong>Wulin Xie</strong>, Rui Dai, Ruidong Ding, Kaikui Liu, Xiangxiang Chu, Xinwen Hou, Jie Wen',en='Making visual reinforcement learning more reliable with uncertainty-aware optimization and perceptual supervision. KADID PLCC / SRCC improves from 0.723 / 0.719 to 0.779 / 0.775 over VisualQuality-R1.',zh='通过不确定性感知优化与感知监督，提高视觉强化学习的可靠性。相较 VisualQuality-R1，KADID 的 PLCC / SRCC 从 0.723 / 0.719 提升至 0.779 / 0.775。',links=[('Paper','https://arxiv.org/abs/2601.22920'),('Code','https://github.com/AMAP-ML/Q-Hawkeye')],selected=True),
 dict(id='rlhf',image='MM-RLHF',tags='rl multimodal',venue='ICML 2025',role=('Core contributor','核心贡献者'),title='MM-RLHF: The Next Step Forward in Multimodal LLM Alignment',authors='Yi-Fan Zhang, Tao Yu, Haochen Tian, Chaoyou Fu, Peiyan Li, Jianshu Zeng, <strong>Wulin Xie</strong>, et al.',en='Multimodal preference alignment with 120K human-annotated preference pairs, critique-based reward modeling, and dynamic preference optimization, evaluated on 27 benchmarks.',zh='围绕 12 万对人工偏好数据、批判式奖励建模与动态偏好优化，推进多模态模型对齐，并在 27 个基准上进行系统验证。',links=[('Paper','https://arxiv.org/abs/2502.10391'),('Project','https://mm-rlhf.github.io/')]),
 dict(id='ocr',image='MME-VideoOCR',tags='multimodal',venue='NeurIPS 2025',role=('Core contributor','核心贡献者'),title='MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios',authors='Yang Shi, Huanqian Wang, <strong>Wulin Xie</strong>, Huanyao Zhang, Lijie Zhao, Yi-Fan Zhang, et al.',en='Beyond reading a single frame: 2,000 human-annotated questions probe text recognition, cross-frame integration, and spatiotemporal reasoning in video.',zh='超越单帧文字识别：通过 2,000 条人工问答，评估视频文字识别、跨帧信息整合与时空推理。',links=[('Paper','https://arxiv.org/abs/2505.21333'),('Project','https://mme-videoocr.github.io/')]),
 dict(id='mvfd',image='MVFD',tags='representation',venue='WACV 2025 · Oral',role=('First author','第一作者'),title='Multi-View Factorizing and Disentangling: A Novel Framework for Incomplete Multi-View Multi-Label Classification',authors='<strong>Wulin Xie</strong>, Lian Zhao, Jiang Long, Xiaohuan Lu, Bingyan Nie',en='Learning shared and view-specific representations under missing views and labels. Evaluated against 10 methods on five datasets, with stronger average precision under 50% missingness.',zh='面向视图与标签同时缺失的情形，学习共享与视图特异表示。在 5 个数据集上对比 10 种方法，提升 50% 缺失条件下的平均精度。',links=[('Paper','https://openaccess.thecvf.com/content/WACV2025/html/Xie_Multi-View_Factorizing_and_Disentangling_A_Novel_Framework_for_Incomplete_Multi-View_WACV_2025_paper.html')],selected=True),
 dict(id='updgd',image='UPDGD-Net',tags='representation',venue='ACM MM 2024',role=('First author','第一作者'),title='Uncertainty-Aware Pseudo-Labeling and Dual Graph Driven Network for Incomplete Multi-View Multi-Label Classification',authors='<strong>Wulin Xie</strong>, Xiaohuan Lu, Yadong Liu, Jiang Long, Bob Zhang, Shuping Zhao, Jie Wen',en='Turning incomplete supervision into reliable learning signals through uncertainty-aware pseudo-labeling and label-guided dual graph constraints, validated on six datasets.',zh='通过不确定性感知伪标签与标签引导的双图约束，将不完全监督转化为可靠学习信号，并在 6 个数据集上验证。',links=[('Paper','https://doi.org/10.1145/3664647.3680932'),('Code','https://github.com/aba122/UPDGD-Net')],selected=True)
]

def paper(p):
    image=(f'<img src="assets/papers/{p["image"]}.png" alt="{escape(p["title"])} — paper figure" loading="lazy" width="420" height="280">' if p['image'] else '<div class="paper-typography"><span>UPDGD</span><small>UNCERTAINTY-AWARE<br>MULTI-VIEW LEARNING</small><div class="graph-mark" aria-hidden="true">◌ — ◉ — ◌</div></div>')
    return f'''<article class="paper {'lead-paper' if p.get('selected') else ''}" data-tags="{p['tags']}" data-id="{p['id']}">
      <a class="paper-image" href="{p['links'][0][1]}" target="_blank" rel="noopener noreferrer" tabindex="-1" aria-hidden="true">{image}</a>
      <div class="paper-content"><div class="paper-meta"><span class="venue {'under-review' if 'Review' in p['venue'] else ''}">{p['venue']}</span><span class="author-role">{bi(*p['role'])}</span></div>
      <h3>{link(p['links'][0][1],p['title'])}</h3><p class="authors">{p['authors']}</p><p class="paper-summary">{bi(p['en'],p['zh'])}</p>
      <div class="paper-links">{''.join(link(url, label+' <span aria-hidden="true">↗</span>') for label,url in p['links'])}</div></div></article>'''

experience=[
 ('longcat.svg','Meituan · LongCat Interaction','美团 · LongCat Interaction',('Beidou Talent Program · Research Intern','北斗计划 · 算法研究实习生'),'2026.04 — '+bi('Present','至今')),
 ('alibaba.png','Alibaba · Amap','阿里巴巴 · 高德地图',('Algorithm Research Intern','算法研究实习生'),'2025.08 — 2026.03'),
 ('vivo.png','vivo','vivo',('Algorithm Research Intern','算法研究实习生'),'2024.12 — 2025.04'),
 ('casia.png','Institute of Automation, CAS','中国科学院自动化研究所',('Research Intern','科研实习生'),'2024.12 — 2025.08'),
 ('hitsz-mobile.png','Harbin Institute of Technology, Shenzhen','哈尔滨工业大学（深圳）',('Research Intern','科研实习生'),'2023.08 — 2024.07'),
]

def exp(row):
    logo,en,zh,role,dates=row
    return f'''<article class="experience"><div class="org-logo {"casia-mark" if logo == "casia.png" else ""}"><img src="assets/logos/{logo}" alt="{en}" loading="lazy" width="64" height="64"></div><div><div class="experience-heading"><h3>{bi(en,zh)}</h3><span class="dates">{dates}</span></div><p class="position">{bi(*role)}</p></div></article>'''

nav=''.join(f'<a href="#{id}"><span class="nav-dot"></span>{bi(en,zh)}</a>' for id,en,zh in [('about','About','关于'),('research','Research','研究'),('publications','Publications','论文'),('experience','Experience','经历'),('education','Education','教育'),('contact','Contact','联系')])
html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wulin Xie | LLMs, Agents & Multimodal Learning</title>
<meta name="description" content="Wulin Xie is a master's student at UCAS and CASIA, researching LLM mid/post-training, agents, and multimodal reinforcement learning.">
<meta name="author" content="Wulin Xie"><meta name="theme-color" content="#faf9f6">
<link rel="canonical" href="https://wulinxie.github.io/">
<meta property="og:url" content="https://wulinxie.github.io/">
<meta property="og:image" content="https://wulinxie.github.io/assets/avatar.jpg">
<meta property="og:title" content="Wulin Xie"><meta property="og:description" content="LLM mid/post-training · Agents · Multimodal learning | UCAS / CASIA"><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css">
<script src="script.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar"><a href="#about" class="wordmark" aria-label="Wulin Xie, top of page">WX<span>.</span></a><span class="topbar-note">{bi('RESEARCH / PERSONAL','研究 / 个人主页')}</span></header>
<nav class="section-nav" aria-label="Page sections">{nav}</nav>
<main id="main">
<section id="about" class="intro">
 <div class="intro-copy"><p class="eyebrow">UCAS &nbsp; / &nbsp; CASIA &nbsp; / &nbsp; BEIJING</p><h1>Wulin Xie</h1>
 <p class="intro-role">{bi('Master’s student · Class of 2028','硕士研究生 · 2028 届')}</p>
 <p>{bi('I am a master’s student in <strong>Pattern Recognition and Intelligent Systems</strong> at the University of Chinese Academy of Sciences and the Institute of Automation, Chinese Academy of Sciences.','我是中国科学院大学、中国科学院自动化研究所<strong>模式识别与智能系统</strong>专业硕士研究生。')}</p>
 <p>{bi('My research focuses on <strong>LLM mid/post-training, agents, and multimodal reinforcement learning</strong>. I am interested in how models learn to reason, use tools, and connect understanding with generation.','我的研究方向是<strong>大模型中后训练、Agent 与多模态强化学习</strong>，关注模型如何学会推理、使用工具，以及协同完成理解与生成。')}</p>
 <p>{bi('I am currently a research intern at <strong>Meituan LongCat Interaction</strong> through the <strong>Beidou Talent Program</strong>, following research internships at Alibaba Amap and vivo.','目前在<strong>美团 LongCat Interaction（北斗计划）</strong>实习，此前曾在阿里高德、vivo 开展算法研究实习。')}</p>
 <div class="contact-links">{link('mailto:xwl1085930920@gmail.com','Email ↗')}{link('https://scholar.google.com/citations?user=paH0IqAAAAAJ','Google Scholar ↗')}{link('https://github.com/aba122','GitHub ↗')}</div>
 </div><aside class="portrait"><img src="assets/avatar.jpg" alt="Portrait of Wulin Xie" width="943" height="1297"></aside>
</section>
<div class="highlights" aria-label="Research highlights"><div><strong>300<span>+</span></strong><span>{bi('Google Scholar citations','Google Scholar 引用')}</span></div><div><strong>4</strong><span>{bi('Accepted first / co-first papers','一作 / 共一已接收论文')}</span></div><div><strong>3</strong><span>{bi('Industry research internships','算法研究实习经历')}</span></div><p class="metrics-note">{bi('As of Sep. 2026','截至 2026 年 9 月')}</p></div>
<section id="research">{section_title('01','Research interests','研究方向')}
<div class="research-grid"><article><span class="research-icon" aria-hidden="true">↗</span><h3>{bi('Learning after pre-training','大模型中后训练')}</h3><p>{bi('Mid-Training, SFT, reinforcement learning, and on-policy distillation for capable, reliable foundation models.','通过 Mid-Training、SFT、强化学习与 OPD，提升基座模型的能力与可靠性。')}</p></article><article><span class="research-icon" aria-hidden="true">⌘</span><h3>{bi('Agents that learn by doing','Agent 学习与交互')}</h3><p>{bi('Tool use, long-horizon interaction, and efficient learning from multi-turn agent experience.','研究工具使用、长程交互，以及从多轮 Agent 经验中高效学习。')}</p></article><article><span class="research-icon" aria-hidden="true">◈</span><h3>{bi('Understanding × generation','多模态理解与生成')}</h3><p>{bi('Unified multimodal evaluation, video understanding, visual reasoning, and preference alignment.','统一多模态评测、视频理解、视觉推理与偏好对齐。')}</p></article></div>
<div class="news"><h3>{bi('Recent highlights','近期动态')}</h3><ul><li><time>2026</time><span>{bi('<strong>VI-Bench</strong> accepted to <strong>NeurIPS 2026</strong> as a first-author paper.','一作论文 <strong>VI-Bench</strong> 被 <strong>NeurIPS 2026</strong> 接收。')}</span></li><li><time>2026.04</time><span>{bi('Joined <strong>Meituan LongCat Interaction</strong> through the Beidou Talent Program.','加入<strong>美团 LongCat Interaction 北斗计划</strong>。')}</span></li><li><time>2026</time><span>{bi('<strong>MME-Unify</strong> accepted to <strong>ICLR 2026</strong> as a co-first-author paper.','共同一作论文 <strong>MME-Unify</strong> 被 <strong>ICLR 2026</strong> 接收。')}</span></li></ul></div>
</section>
<section id="publications">{section_title('02','Selected publications','代表论文',link('https://scholar.google.com/citations?user=paH0IqAAAAAJ',bi('All on Scholar ↗','Scholar 完整列表 ↗'),'section-more'))}
<p class="section-intro">{bi('A selection of my work on learning, alignment, and evaluation. First / co-first-author work is highlighted.','围绕模型学习、对齐与评测的代表工作。浅色背景标记一作 / 共一论文。')}</p>
<div class="filters" role="group" aria-label="Filter publications"><button class="active" data-filter="all" aria-pressed="true">{bi('All','全部')} <span>7</span></button><button data-filter="rl" aria-pressed="false">{bi('RL & alignment','强化学习与对齐')} <span>2</span></button><button data-filter="multimodal" aria-pressed="false">{bi('Multimodal','多模态')} <span>5</span></button><button data-filter="representation" aria-pressed="false">{bi('Representation learning','表示学习')} <span>2</span></button></div>
<p id="filter-status" class="sr-only" role="status" aria-live="polite">7 publications</p>
<div class="paper-list">{''.join(paper(p) for p in papers)}</div>
<details class="other-papers"><summary>{bi('Additional research & journal articles','其他研究与期刊论文')} <span aria-hidden="true">+</span></summary><ul><li><strong>A Survey of Unified Multimodal Understanding and Generation: Advances and Challenges</strong><p>Y. Yang, H. Tian, Y. Shi, <strong>Wulin Xie</strong>, et al. · TPAMI · Under Review</p></li><li><strong>Confidence-Enhanced Dual-Space Semantic Alignment for Partial Multi-View Incomplete Multi-Label Classification</strong><p>J. Chen, <strong>Wulin Xie</strong>, et al. · Knowledge-Based Systems</p></li><li><strong>Cross-modal mapping: Mitigating the modality gap for few-shot classification</strong><p>X. Yang, <strong>Wulin Xie</strong>, et al. · Pattern Recognition</p></li></ul></details>
</section>
<section id="experience">{section_title('03','Research experience','实习与科研经历')}<div class="experience-list">{''.join(exp(e) for e in experience)}</div></section>
<section id="education">{section_title('04','Education','教育背景')}
<div class="education-entry"><span class="education-year">2025 — 2028</span><div><h3>{bi('University of Chinese Academy of Sciences','中国科学院大学')}</h3><p>{bi('Institute of Automation, Chinese Academy of Sciences','中国科学院自动化研究所')}</p><p>{bi('M.Sc. in Pattern Recognition and Intelligent Systems · Expected Jul. 2028','模式识别与智能系统硕士 · 预计 2028 年 7 月毕业')}</p></div></div>
</section>
<section id="contact" class="contact-section"><p class="eyebrow">{bi('LET’S CONNECT','保持联系')}</p><h2>{bi('Building models that do more.','让模型理解更多，也做到更多。')}</h2><p>{bi('I’m looking for research internships in foundation models, agents, and multimodal learning. If our interests overlap, I’d love to hear from you.','我正在寻找基座模型、Agent 与多模态方向的研究实习机会，欢迎交流与联系。')}</p>{link('mailto:xwl1085930920@gmail.com','xwl1085930920@gmail.com <span aria-hidden="true">↗</span>','contact-email')}</section>
</main>
<footer class="mountain-footer"><div class="footer-overlay"><p class="footer-title">{bi('Keep exploring.','保持好奇，持续探索。')}</p><p>Wulin Xie</p><div class="footer-meta"><span>{bi('Updated September 2026','更新于 2026 年 9 月')}</span><span>{bi('Design inspired by','设计参考')} {link('https://github.com/w-r-s/academic-homepage-template','w-r-s / academic-homepage-template')}</span></div></div></footer>
<a id="back-top" href="#about" aria-label="Back to top">↑</a>
</body></html>'''
(ROOT/'index.html').write_text(html)
print('Built index.html: 7 featured publications, 5 experience entries, English only')
