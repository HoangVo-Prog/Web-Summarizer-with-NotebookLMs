VNFD_PATH = "VFND-vietnamese-fake-news-datasets/Dataset"



prompt_task1_en_with_desc = f"""
You are a fact-checking expert. Based on the metadata and full content of a Vietnamese news article, assess whether the information is factual (Label = 1), false/misleading (Label = 0), or ambiguous/uncertain (Label = -1). Return:
- Label: 1 (true), 0 (false), or -1 (ambiguous)
- Justification (in Vietnamese): a concise explanation based on logic, public facts, or scientific evidence.

Use the metadata below to support your assessment.

📄 ARTICLE DATA:
- authors: The author(s) of the article.
- date_publish: The date the article was originally published.
- source_domain: The website or domain that published the article (e.g., tuoitre.vn, thoibao.de).
- title: The headline or title of the article, often summarizing the claim.
- maintext: The full body of the article, which contains the information or narrative to verify.
- language: The language of the article (should be 'vi' for Vietnamese).
- url: The original URL to the article (for source traceability).

🔍 TASK:
Evaluate whether the article contains factual or misleading information.
- Use public sources, logic, or science to justify your answer.
- If the article contains speculative, satirical, opinion-based, or unverifiable claims, assign **Label = -1** and explain why it cannot be clearly fact-checked.

📝 Return your response in the format:
Label: -1 / 0 / 1  
Justification: [in Vietnamese]

---

✅ Examples:

Example 1:  
Title: "Uống nước ép cần tây có thể chữa khỏi ung thư."  
Source: khoedep24h.net  
Label: 0  
Justification: Hiện chưa có bằng chứng khoa học nào cho thấy nước ép cần tây có thể chữa ung thư. Đây là thông tin sai lệch thường được chia sẻ sai mục đích.

Example 2:  
Title: "Việt Nam là nước xuất khẩu hồ tiêu lớn nhất thế giới năm 2023."  
Source: vnexpress.net  
Label: 1  
Justification: Đây là dữ liệu đã được xác nhận trong báo cáo thương mại quốc tế. Việt Nam dẫn đầu về xuất khẩu hồ tiêu toàn cầu nhiều năm qua.

Example 3:  
Title: "NASA xác nhận Trái Đất sẽ chìm trong bóng tối 3 ngày vào tháng 6."  
Source: tinla.vn  
Label: 0  
Justification: NASA chưa bao giờ công bố điều này. Đây là tin giả cũ từng bị bác bỏ. Không có cơ sở khoa học để hiện tượng này xảy ra.

Example 4:  
Title: "Người ngoài hành tinh từng liên lạc với chính phủ Việt Nam năm 1972."  
Source: blogtintuc.net  
Label: -1  
Justification: Đây là tuyên bố không có bằng chứng xác thực, mang tính giả định hoặc thuyết âm mưu. Không thể kiểm chứng tính đúng sai.

---

📝 Evaluate the following article:

Title: {title}  
Source: {source_domain}  
Date: {date_publish}  
Language: {language}  
Authors: {authors}  
URL: {url}  

Main Content:  
{maintext}

Your response:  
Label:  
Justification:
"""
