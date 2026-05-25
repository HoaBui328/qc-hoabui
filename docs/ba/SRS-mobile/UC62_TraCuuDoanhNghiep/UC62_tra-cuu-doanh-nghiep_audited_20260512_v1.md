# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC62_tra-cuu-doanh-nghiep_srs_20260512_v1.md`

---

## Feature Brief
Chức năng đóng vai trò danh bạ kết nối giao thương, hỗ trợ nhà đầu tư tra cứu thông tin công ty, đối tác. Bao gồm luồng duyệt danh sách dạng thẻ (hiển thị nhu cầu kết nối), tìm kiếm qua bộ lọc đa điều kiện, và màn hình hồ sơ công ty chi tiết hiển thị tổng quan, năng lực, cũng như cung cấp lối tắt mở Intent ra Trình duyệt/Mail của thiết bị.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `91.0 / 100` | ⚡ **CONDITIONALLY READY** |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --------- | ----------------------------------------- | --------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 16/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 17/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 9/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | | **101/110 → 91.8/100 (Adjusted to 91.0 cho các Gaps)** |

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *UI Danh sách vs Bộ lọc* | Trên màn hình Danh sách, có 1 thẻ tag Filter nằm ngang: `Tất cả` và `Đã xác minh`. Tuy nhiên, trong Popup "Bộ lọc tìm kiếm", **KHÔNG CÓ** tuỳ chọn lọc "Đã xác minh". Vậy thẻ `Đã xác minh` ở list là một nút Quick-filter (nhấn vào để lọc ngay lập tức) hay chỉ là text tĩnh báo hiệu? Nếu là Quick-filter, behavior của thanh ngang này thế nào (cuộn ngang)? | Thiếu đồng bộ giữa List UI và Modal Filter UI. Ảnh hưởng đến việc viết AC cho bộ lọc. | Open |
| Q2 | Medium | *Data Mapping (Nhu cầu)* | Ngoài List card, nhu cầu kết nối hiển thị tag rất ngắn (VD: `Đang tìm: Nhà phân phối`). Trong khi ở Màn hình chi tiết, mục Nhu cầu là 1 đoạn text dài (VD: `Tìm kiếm đại lý phân phối cấp 1 toàn quốc...`). Hệ thống Client lấy tag ngắn này ở đâu? (API cấp thêm 1 trường `shortNeedTag` hay Client phải tự xử lý cắt chữ?). | Đảm bảo tính nhất quán dữ liệu giữa màn danh sách và chi tiết. Cắt chữ sai có thể làm mất nghĩa. | Open |
| Q3 | Medium | *Hiển thị Sản phẩm/Dịch vụ* | Trong Hồ sơ công ty, danh sách Tag "Sản phẩm / Dịch vụ chính" có giới hạn số lượng hiển thị tối đa không? (VD công ty có 50 sản phẩm thì có hiện nút "Xem thêm" hay cuộn xuống vô tận?). | Tránh vỡ layout UI nếu số lượng Tag trả về từ API quá lớn. | Open |
| Q4 | Low | *Exception Handling (Missing Data)* | Trong phần "Thông tin liên hệ" ở Hồ sơ, nếu công ty đó chưa cập nhật Email hoặc Website thì UI sẽ xử lý thế nào? (Ẩn luôn cả dòng chữ đó đi, hay hiển thị chữ xám "Đang cập nhật" và disable hành động bấm mở App?). | Cần quy định rõ Empty State của từng field liên hệ. | Open |

---

## 🟢 What's Good
- Áp dụng đầy đủ và chuẩn xác các rule CMR phức tạp (Debounce tìm kiếm, Lazy load list 20 items, Fallback avatar text).
- Cơ chế gọi OS Intent được định nghĩa chặt chẽ (đặc biệt là mailto:// và web browser), đảm bảo không nhầm lẫn với việc mở in-app webview.
- Cấu trúc "Hồ sơ công ty" phân rã theo 3 Section cực kỳ dễ hiểu, map đúng với các highlight box.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Tìm kiếm Textbox (Debounce và Trim khoảng trắng).
- Chức năng Dropdown của Bộ lọc ở Bottom Sheet.
- Lazy load, empty state của danh sách doanh nghiệp.
- Thao tác call OS Intent mở Browser/Mail app từ màn hình hồ sơ chi tiết.

**What CANNOT be tested yet (blocked by gaps):**
- Tính năng lọc nhanh bằng tag `Đã xác minh` trên danh sách.
- Giới hạn hiển thị thẻ Sản phẩm/Dịch vụ.

**Suggested test focus areas (once gaps are resolved):**
- UI Boundary Test: Các doanh nghiệp có tên siêu dài hoặc địa chỉ siêu dài (kiểm tra wrap text).
- Data mapping: Đảm bảo thông số Highlight (Năm thành lập, Nhân sự) ở màn Detail luôn khớp với data trả về ngoài màn List (Quy mô).

---

## 📌 Summary & Recommendation
SRS UC62 v1.0 đạt điểm **91.0/100 (CONDITIONALLY READY)**. Tài liệu được thiết kế rất tốt, tuy nhiên xuất hiện sự **Bất đồng bộ thiết kế (Q1)** giữa màn hình List (có quick filter `Đã xác minh`) nhưng trong Bottom Sheet lại không hỗ trợ field này. Xin vui lòng phản hồi 4 câu hỏi trên để hoàn thiện luồng và nâng cấp lên phiên bản v2.0.
