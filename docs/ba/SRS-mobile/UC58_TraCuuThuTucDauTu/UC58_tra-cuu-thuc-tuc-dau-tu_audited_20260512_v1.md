# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC58_tra-cuu-thuc-tuc-dau-tu_srs_20260512_v2.md`

---

## Feature Brief
Chức năng cho phép nhà đầu tư tìm kiếm, lọc (theo Lĩnh vực, Cấp thực hiện, Mức độ, Thời gian) và tra cứu thông tin chi tiết về các thủ tục đầu tư. Hệ thống hiển thị dưới dạng 3 tab: Thông tin chung (với các khối Highlight thông số), Trình tự thực hiện (Timeline), và Thành phần hồ sơ (Bắt buộc/Tùy chọn).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `89.0 / 100` | ⚡ **CONDITIONALLY READY** |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --------- | ----------------------------------------- | --------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 17/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 18/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | | **103/110 → 93.6/100 (Adjusted to 89 cho các open questions)** |

*(Lưu ý: Mặc dù score thô là 93.6 (Ready), nhưng do còn thiếu một vài action cụ thể của thành phần nội dung nên kết quả được hạ xuống 89.0 - Conditionally Ready).*

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | Medium | *Tab Thông tin chung -> Block Căn cứ pháp lý* | Tap vào các dòng Căn cứ pháp lý (VD: Luật Đầu tư 2020) có mở ra màn hình chi tiết văn bản, link trình duyệt, hay chỉ hiển thị text tĩnh thông thường? | QA cần biết để viết test case verify link điều hướng nếu có. | Open |
| Q2 | Medium | *Tab Trình tự thực hiện -> Timeline* | Khi phần mô tả hành động của một bước (Timeline nội dung) quá dài, hệ thống có tự động hiển thị `...` kèm nút "Xem thêm", hay đẩy layout dài vô tận? | Đảm bảo tính toàn vẹn của UI khi API trả về text siêu dài (Edge case Group A). | Open |
| Q3 | Low | *Ngôn ngữ (CMR-17)* | Khi người dùng đổi ngôn ngữ hệ thống, setting ngôn ngữ này được lưu tại Local Storage của máy hay được sync qua API? | Cần thiết để tester test logic persistence ngôn ngữ sau khi cài đặt lại app. | Open |

---

## 🟢 What's Good
- Tài liệu cực kỳ chi tiết, tuân thủ tuyệt đối chuẩn định dạng 7 cột và các CMR rule.
- Đã cover toàn bộ các flow edge case: Debounce, Lazy load tự retry 3 lần, State Persistence.
- Đã kịp thời lược bỏ nút "Nộp hồ sơ" để đảm bảo đúng scope Tra cứu.
- AC và Logic lỗi được định nghĩa rõ ràng, cụ thể.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Toàn bộ luồng danh sách, tìm kiếm (debounce 3s), lọc dữ liệu (bao gồm rule Date Picker của CMR-15).
- Các thao tác UI: Swipe đổi tab, Lazy load, Skeleton, State Persistence khi back ra.
- Hiển thị data: Các badge thông số, danh sách hồ sơ bắt buộc/tùy chọn, format tiền tệ.

**What CANNOT be tested yet (blocked by gaps):**
- Hành vi tương tác ở mục Căn cứ pháp lý.
- Xử lý text quá dài ở luồng Timeline.

**Suggested test focus areas (once gaps are resolved):**
- Happy path: Xem chi tiết 3 tab.
- Filter Boundary: Test case "Từ ngày lớn hơn Đến ngày" sẽ bị chặn.
- Đa ngôn ngữ UI: Chuyển đổi ngôn ngữ máy xem label tĩnh (Ví dụ: "Thành phần hồ sơ") có đổi tức thì không.
- Partial Failure API: Chặn API ở Tab 2 xem Tab 1 và 3 có render bình thường không.

---

## 📌 Summary & Recommendation
Tài liệu SRS UC58 phiên bản v2.0 có chất lượng xuất sắc, đạt điểm đánh giá **89.0/100 (CONDITIONALLY READY)**. Các luồng chính đều rõ ràng, mạch lạc và sẵn sàng để viết Test Case. Đội QA có thể bắt đầu làm việc ngay. Có 3 câu hỏi (Gap) nhỏ được trích xuất để BA confirm thêm về hành vi UI/UX.
