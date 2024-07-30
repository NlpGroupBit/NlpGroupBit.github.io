+++
abstract = "Sentiment classification is a form of data analytics where people’s feelings and attitudes toward a topic are mined from data. This tantalizing power to “predict the zeitgeist” means that sentiment classification has long attracted interest, but with mixed results. However, the recent development of the BERT framework and its pretrained neural language models is seeing new-found success for sentiment classification. BERT models are trained to capture word-level information via mask language modeling and sentence-level contexts via next sentence prediction tasks. Out of the box, they are adequate models for some natural language processing tasks. However, most models are further fine-tuned with domain-specific information to increase accuracy and usefulness. Motivated by the idea that a further fine-tuning step would improve the performance for downstream sentiment classification tasks, we developed TopicBERT—a BERT model fine-tuned to recognize topics at the corpus level in addition to the word and sentence levels. TopicBERT comprises two variants: TopicBERT-ATP (aspect topic prediction), which captures topic information via an auxiliary training task, and TopicBERT-TA, where topic representation is directly injected into a topic augmentation layer for sentiment classification. With TopicBERT-ATP, the topics are predetermined by an LDA mechanism and collapsed Gibbs sampling. With TopicBERT-TA, the topics can change dynamically during the training. Experimental results show that both approaches deliver the state-of-the-art performance in two different domains with SemEval 2014 Task 4. However, in a test of methods, direct augmentation outperforms further training. Comprehensive analyses in the form of ablation, parameter, and complexity studies accompany the results."
date = "2023-01-01"
image = ""
image_preview = ""
math = false
publication = "IEEE Transactions on Neural Networks and Learning Systems"
publication_short = ""
selected = false
title = "TopicBERT: A Topic-Enhanced Neural Language Model Fine-Tuned for Sentiment Classification"
url_dataset = ""
url_pdf = "https://ieeexplore.ieee.org/document/9508773"
url_slides = ""
url_video = ""

[[authors]]
    name = "Yuxiang Zhou"
    is_member = false
[[authors]]
    name = "Leijian Liao"
    is_member = false
[[authors]]
    is_member = true
    id = "member1"
[[authors]]
    name = "Rui Wang"
    is_member = false
[[authors]]
    name = "Heyan Huang"
    is_member = false

    

+++
