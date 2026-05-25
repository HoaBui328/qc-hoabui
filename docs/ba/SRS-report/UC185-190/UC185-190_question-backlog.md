# Question Backlog

> Generated: 2026-05-11
> Source files: UC185-190_BaoCaoNamDTRNN.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *Mô tả chức năng UC185-190.2: "Phân quyền: Nhà đầu tư (ĐTRNN) được phép tạo báo cáo trong kỳ hiện tại hoặc kỳ đã qua (Trong thời hạn / Qua kỳ báo cáo). Không được phép tạo báo cáo cho kỳ Chưa tới hạn. Tham chiếu: CMR_04."* | **Mâu thuẫn với quy tắc chung CMR_04**. CMR_04 định nghĩa rõ: "Qua kỳ báo cáo: Ẩn nút [Lập báo cáo] và [Import]". Việc UC185-190 cho phép lập "Qua kỳ báo cáo" là vi phạm rule hệ thống. BA cần xác nhận lại: cho phép lập qua hạn hay khóa theo CMR_04? | Ảnh hưởng trực tiếp đến logic ẩn/hiện nút Tạo mới. Dev không biết code theo UC hay theo CMR. | Open |
| Q2 | Medium | *CS_01 Mục 4: Empty States Logic - Kỳ hạn chưa tới: Hiển thị thông báo: "Kỳ báo cáo này chưa tới hạn..."* VÀ *UC185-190.1: "Empty state khi không có dữ liệu lần đầu: hiển thị text 'Chưa có báo cáo nào. Nhấn [Lập báo cáo] để bắt đầu.'"* | Text Empty state trong UC đang bị fix cứng và mâu thuẫn với CS_01 (vốn chia ra 3 trạng thái empty khác nhau: Chưa tới, Trong kỳ, Qua kỳ). Cần tuân thủ hoàn toàn CS_01? | Gây mâu thuẫn UI giữa các màn hình danh sách. | Open |
| Q3 | Medium | *UC185-190.1: "Kỳ báo cáo (Năm) - Tham chiếu: CMR_08."* | Tài liệu CMR_08 hiện tại ghi rõ: "(Chưa định nghĩa — Chờ BA xác nhận: tên kỳ, định dạng hiển thị, logic nhóm.)". BA cần bổ sung định nghĩa CMR_08. | Tester không có cơ sở để thiết kế test case cho phần cấu trúc và định dạng Kỳ báo cáo. | Open |
| Q4 | Medium | *Field 30: Lợi nhuận (Nhóm 3)* và *Field 40: Tiền giữ lại tái đầu tư (Nhóm 5)* | Field 40 yêu cầu validate "≤ Lợi nhuận (trường 30) của cùng năm báo cáo (cột Năm BC)". Tuy nhiên, Nhóm 3 (Lợi nhuận) không nói rõ có phân tách cột theo từng NĐT như Nhóm 1 hay không. Nếu Lợi nhuận là dòng tổng của toàn dự án, thì việc validate tái đầu tư của "từng NĐT" với Lợi nhuận "của toàn dự án" hay "của cùng NĐT đó" đang bị mù mờ. Cần làm rõ cấu trúc cột Nhóm 3. | Không thể thiết kế test case cho validate cross-field giữa Nhóm 5 và Nhóm 3. | Open |
| Q5 | Medium | *CF_06 (Xem vòng đời)* | Tài liệu ghi: "Chi tiết cấu trúc timeline và các loại hành động: Chưa xác định, sẽ được cập nhật sau." | Thiếu logic về nội dung cụ thể trong màn Audit Trail để thiết kế test. | Open |
| Q6 | Low | *Tên nút [Xem] (field 57 trong UC185-190.2)* | Field 57 ghi nút là "Xem". Tuy nhiên CF_07.1 gọi nút này trong màn View là "Xem", nhưng trong CF_01 (Tạo mới) thì quy tắc chung lại là "Xem chi tiết". Cần chuẩn hóa tên nút trên màn Create. | Gây nhầm lẫn trong tài liệu UI. | Open |
| Q7 | Medium | *Field 8: Năm báo cáo* | Validate: "số nguyên 4 chữ số và ≤ năm hiện tại". Cần làm rõ: có được phép báo cáo cho năm hiện tại khi chưa kết thúc năm không? Có validate giới hạn dưới không (VD: không được nhập năm < 1900)? | Cần thiết kế test data boundary (năm biên giới hạn). | Open |
| Q8 | Medium | *UC185-190.2: Thiếu mô tả luồng Import* | UC185-190.1 có nhắc đến nút [Import] bị ẩn khi Chưa tới hạn. Tuy nhiên UC185-190.2 hoàn toàn không có Field/Button nào nhắc đến việc Import, dù báo cáo này áp dụng CF_02. | Cần bổ sung UI object và workflow cho Import trong UC185-190.2 để QA viết test. | Open |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
