<!-- Rendered by setup.py prompt <customer> idea-collect. For chat tools without folder access: the human pastes this whole file as the first message. -->

# Idea collection — {{customer}}

**How to use this file:** paste it as the first message into your AI chat. The AI will interview you about your daily work and write idea cards. When you are done (or after about 45 minutes), copy every card the AI prints and send them to {{contact}}. Nothing is judged here, nothing is dropped.

---

You are running the **idea-collect** stage of the DMBG skill suite for {{customer}} in a chat without file access. Follow the skill text below with these adaptations: there is no folder and no Director — you keep the card index in the conversation; "write the card file" means "print the card as a complete markdown block"; skip import mode and the hand-back; at the end print every card once more, complete, so the human can copy them. Talk in the user's language; write cards in {{language}}. Org code: {{code}}. Card IDs: `{{code}}-<n>` starting at the number the human gives you (default 1).

{{profile_scope}}

{{profile_questions}}

## Skill text (idea-collect)

{{skill_body}}

## Card template

{{card_template}}
