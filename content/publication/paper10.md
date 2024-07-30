+++
abstract = "Parallel cross-lingual summarization data is scarce, requiring models to better use the limited available cross-lingual resources. Existing methods to do so often adopt sequence-to-sequence networks with multi-task frameworks. Such approaches apply multiple decoders, each of which is utilized for a specific task. However, these independent decoders share no parameters, hence fail to capture the relationships between the discrete phrases of summaries in different languages, breaking the connections in order to transfer the knowledge of the high-resource languages to low-resource languages. To bridge these connections, we propose a novel Multi-Task framework for Cross-Lingual Abstractive Summarization (MCLAS) in a low-resource setting. Employing one unified decoder to generate the sequential concatenation of monolingual and cross-lingual summaries, MCLAS makes the monolingual summarization task a prerequisite of the cross-lingual summarization (CLS) task. In this way, the shared decoder learns interactions involving alignments and summary patterns across languages, which encourages attaining knowledge transfer. Experiments on two CLS datasets demonstrate that our model significantly outperforms three baseline models in both low-resource and full-dataset scenarios. Moreover, in-depth analysis on the generated summaries and attention heads verifies that interactions are learned well using MCLAS, which benefits the CLS task under limited parallel resources."
date = "2021-05-28"
image = ""
image_preview = ""
math = false
publication = "ACL 2021"
publication_short = ""
selected = false
title = "Cross-Lingual Abstractive Summarization with Limited Parallel Resources"
url_dataset = ""
url_pdf = "https://arxiv.org/abs/2105.13648"
url_slides = ""
url_video = ""

[[authors]]
    is_member = true
    id = "member3"
[[authors]]
    is_member = true
    id = "member1"
[[authors]]
    name = "Heyan Huang"
    is_member = false
+++
