# Viera Agent Workflow · v3.0.2

**DC-PKT-02** · [English](README.md) · [Phạm vi tương thích](COMPATIBILITY.md)

Gói giúp agent tiếp tục từ checkpoint, nhận ra việc đã làm, kiểm đúng artifact trên đường chạy cần giao và bàn giao qua hồ sơ sẵn có. Năm skill dùng chung một workflow. [AGENTS.md](AGENTS.md) là nguồn luật chuẩn. Dự án giữ nguyên quyền, nghĩa vụ riêng, cổng chất lượng và cơ chế bàn giao hiện có.

## Thử trên ví dụ tổng hợp

Giải nén ZIP hoặc mở bản checkout sạch ở tag `v3.0.2`. Từ thư mục gốc, dùng Python 3.10 trở lên chạy `python -X utf8 kiem_tra_goi.py`. Mở [ví dụ DEMO](examples/README.md) để xem cách đọc cây, packet và checkpoint qua một lượt bàn giao. Ví dụ dùng danh tính giả lập và không cấp quyền ghi.

## Áp dụng cho một dự án

1. **Xác định việc được giao.** Gửi ZIP ngoài đường tự nạp của dự án. Ghi phạm vi vào task hiện có theo `LENH_AP_DUNG.txt` nếu cần soạn, thử hoặc chuyển nguồn. Gửi ZIP để xem xét chỉ cho phép xem xét.
2. **Điền binding và chốt phần thay.** Dùng mẫu ở mục 2 của `CHUYEN_DOI_LUAT_VA_TIEP_TUC.md`. Tìm nguồn thực đang hiệu lực, các ghi chú global/parent/nested, cây, task/journal, writer, workflow và nơi giữ bản phục hồi. Ghi từng mục giữ, thay hoặc nghỉ hưu và dự kiến kiểm mục đó thế nào.
3. **Chọn đường workflow.** Codex mở repo này sẽ tìm năm điểm gọi trong `.agents/skills/`. Khi cài vào dự án khác, kiểm trùng tên và chỉ dùng năm thư mục con tại `.agents/skills/` cho Codex. Vị trí được Claude Code mô tả là `.claude/skills/`, dùng cùng năm thư mục và kiểm client trước khi áp dụng. Giữ một `QUY_TRINH_SKILL_VA_AGENT.md` và ghim đường dẫn của nó trong binding dự án. `CLAUDE.md` với `@AGENTS.md` là cầu nối tùy client. Gỡ thử nghiệm bằng cách khôi phục binding và đúng các điểm gọi đã thay, rồi mở phiên mới để kiểm nguồn cũ.
4. **Thử trước khi mở tác động phụ thuộc.** Dùng HK01–HK12 trong `LENH_CODEX_KIEM_TRA_SAU_THAY_LUAT.txt` theo phần chịu ảnh hưởng. Kiểm nạp đến cuối nguồn, trigger workflow, cây, bàn giao, quyền ghi và khôi phục theo scope. Ghi `NOT_RUN` cho client chưa chạy. Cài và chuyển nguồn khi được giao và đạt cổng áp dụng. Sau chuyển xác nhận lại nguồn thực nạp trên phiên mới. Bàn giao và nhả phần giữ bằng lifecycle đang dùng.

Khi thiếu một nguồn bắt buộc, giữ bước phụ thuộc và ghi checkpoint. Tiếp phần độc lập đã được giao. Khi làm thường ngày, dùng R18 của `AGENTS.md`. Chỉ mở quy trình migration khi đổi luật, binding hoặc cấu hình ảnh hưởng đường nạp.

## Giới hạn kiểm chứng

Codex app-server `0.171.0-alpha.13` trên Windows đã nhận diện và gọi đủ năm skill trên mẫu. Codex Desktop GUI và CLI độc lập chưa chạy trên ứng viên này. Claude Code mới kiểm tĩnh cấu trúc và đường dẫn. Host chưa cung cấp model và mức suy luận thực thi ở backend. Hiệu quả trên sản phẩm và mức tiết kiệm vẫn chưa được chứng minh. Cơ chế ghi và nhả quyền phụ thuộc host và dự án.

## Tra cứu trong gói

| Tệp | Công dụng |
|---|---|
| `AGENTS.md` và `CLAUDE.md` | Luật HOST R01–R22 và cầu nối cùng nguồn |
| `QUY_TRINH_SKILL_VA_AGENT.md` và `.agents/skills/` | Năm mục thao tác chuẩn, vai theo rủi ro và điểm gọi skill native |
| `CHUYEN_DOI_LUAT_VA_TIEP_TUC.md` và `LENH_AP_DUNG.txt` | Binding, đối chiếu nghĩa vụ, quyền, chuyển nguồn và phục hồi |
| `LENH_CODEX_KIEM_TRA_SAU_THAY_LUAT.txt` | Mười hai ca kiểm theo phần bị tác động |
| `Gui_ChatGPT_MAU_DU_AN.md` | Mẫu packet cho mỗi dự án theo R19, gồm snapshot và nội dung quy tắc điều phối |
| `COMPATIBILITY.md`, `MANIFEST.json`, `kiem_tra_goi.py` | Phạm vi chứng cứ và kiểm toàn vẹn |

Kiểm byte bằng `python -X utf8 kiem_tra_goi.py` từ thư mục đã giải nén, hoặc truyền đường dẫn ZIP làm đối số. Dùng Python 3.10 trở lên. Có thể đối chiếu SHA-256 bằng công cụ sẵn có. Manifest kiểm byte và danh mục. Quyền và chấp thuận lấy từ chỉ thị Owner có hiệu lực.

Ghi trong task theo từng client: **đã cài**, **đã nạp**, **đã kiểm hành vi**. Ghi **nguồn active đã xác nhận** riêng cho từng dự án, với revision, phạm vi, chứng cứ và điều kiện còn thiếu.
