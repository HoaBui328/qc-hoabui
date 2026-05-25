# Question Backlog

> Generated: 2026-05-11
> Source files: UC209-214_DKGDNHChamDutDTRNN_audited_20260511_v1.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *Mục 2 - Bảng 1 (Hình thức ĐT: Dropdown) vs Bảng 2 (Hình thức ĐT: Textbox)* | Cột "Hình thức ĐT" ở Bảng 1 là Dropdown (5 options cố định), nhưng ở Bảng 2 lại là Textbox nhập tay tự do. Đây là yêu cầu nghiệp vụ thực tế hay là lỗi đánh máy? | Cần đồng nhất kiểu dữ liệu hoặc hiểu rõ lý do để kiểm thử giá trị đầu vào hợp lệ. | Open |
| Q2 | High | *Mục 3 (Validate khi Nộp): "Bảng 1 và Bảng 2 được phép rỗng... Không bắt buộc ≥ 1 dòng" vs Mục 2: "Tối thiểu 1 dòng"* | UC ghi bảng tối thiểu 1 dòng khởi tạo. Nếu người dùng không nhập gì vào dòng này và bấm Nộp thì hệ thống có bắt lỗi "Trường bắt buộc" cho các ô trong dòng đó không, hay cho phép Nộp bảng với 1 dòng trống? Người dùng có được phép xoá dòng duy nhất đó để bảng có 0 dòng không (do CMR_15 không cho xoá dòng cuối)? | Ảnh hưởng tới test case Nộp báo cáo không phát sinh nghiệp vụ. Tester cần biết kết quả mong đợi khi bấm Nộp với 1 dòng trống. | Open |
| Q3 | High | *Mục 2 - Bảng Danh sách: "Trạng thái báo cáo" có đủ 4 trạng thái* | UC quy định filter có "Chờ duyệt / Đã tiếp nhận". Theo CMR_03, Nộp xong sẽ rẽ nhánh vào 1 trong 2 tùy quy trình (2 bước hoặc >2 bước). Quy trình duyệt nội bộ của Mẫu II.5 gồm mấy bước? Nộp xong chuyển thẳng sang Đã tiếp nhận hay phải qua Chờ duyệt? | Tester không thể thiết kế luồng trạng thái đúng (State Transition) nếu không biết quy trình duyệt. | Open |
| Q4 | Medium | *Mục 2 - Bảng 1 & Bảng 2 (Mã số DN / CCCD)* | Validate hiện tại chỉ là "Không rỗng" (CMR_06). Có cần validate rule đặc thù (VD: chỉ nhập số, độ dài 10-13 cho mã DN, 12 cho CCCD) không? Việc dùng chung 1 trường cho cả mã DN và CCCD dễ dẫn tới dữ liệu rác. | Bổ sung validate để QA có cơ sở bắt lỗi định dạng. | Open |
| Q5 | Medium | *Mục 2 - HEADER (Số văn bản)* | Trường "Số văn bản" có áp dụng bộ quy tắc nhập/định dạng công văn theo chuẩn `CMR_13` không? | Nếu áp dụng CMR_13, cần test các ký tự đặc biệt, auto-uppercase, định dạng dấu `/`, `-`. | Open |
| Q6 | Medium | *Bảng thuộc tính - Cơ quan nhận: Bộ Tài chính (Cục Đầu tư nước ngoài)* | Báo cáo này nộp cho cơ quan ngoài bộ (Bộ Tài chính). Việc Nộp có liên thông/gọi API gửi dữ liệu sang hệ thống của BTC không, hay chỉ lưu nội bộ trên hệ thống MBFS? | Ảnh hưởng đến việc thiết kế test Integration và mô phỏng (mock) API bên thứ 3. | Open |
| Q7 | Medium | *Mục 3 - Mô tả các xử lý chung: "Phân trang theo số năm / trang"* | Ở CMR_10 quy định "List có kỳ hạn: Phân trang theo Kỳ". Báo cáo này nhóm theo năm, mỗi năm có 12 kỳ. Vậy phân trang theo "số năm / trang" nghĩa là 1 trang hiển thị 10 Năm (120 kỳ) hay 10 Kỳ (không chẵn năm)? | Đảm bảo tính nhất quán của giao diện Danh sách. | Open |
| Q8 | Medium | *Mục 2 - Bảng 1 & 2 (Quốc gia / vùng lãnh thổ)* | Trường "Quốc gia / vùng lãnh thổ" lấy "Danh mục quốc gia chuẩn từ hệ thống". Danh mục này được cung cấp qua API (Master Data) hay fix cứng (Static)? | Cần xác nhận để QC lấy đúng danh mục kiểm tra tính đúng đắn khi hiển thị trên Dropdown. | Open |
| Q9 | Low | *Mục 2 - Bảng 1 (Vốn ĐTRNN > 0) vs Bảng 2 (Vốn đã chuyển ra NN ≥ 0)* | Bảng 1 bắt buộc Vốn > 0. Nếu nhập = 0 sẽ báo lỗi "Giá trị phải lớn hơn 0". Bảng 2 bắt buộc Vốn ≥ 0 (tức là cho phép nhập 0). Điều này có chính xác không? | Cần xác nhận mốc biên giới hạn 0 của hai cột này có thực sự khác nhau không để thiết kế test case Boundary Value. | Open |

Priority: High (blocks design), Medium (affects scope), Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
