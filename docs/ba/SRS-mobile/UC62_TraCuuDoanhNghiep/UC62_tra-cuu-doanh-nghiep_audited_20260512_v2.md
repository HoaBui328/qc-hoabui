# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC62_tra-cuu-doanh-nghiep_srs_20260512_v2.md`

---

## Feature Brief
Chức năng đóng vai trò danh bạ kết nối giao thương, hỗ trợ nhà đầu tư tra cứu thông tin công ty, đối tác. Bao gồm luồng duyệt danh sách dạng thẻ (hiển thị nhu cầu kết nối), tìm kiếm qua bộ lọc đa điều kiện, và màn hình hồ sơ công ty chi tiết hiển thị tổng quan, năng lực, cũng như cung cấp lối tắt mở Intent ra Trình duyệt/Mail của thiết bị.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `100.0 / 100` | ✅ **READY** |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --------- | ----------------------------------------- | --------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | | **110/110 → 100.0/100** |

*(Lưu ý: Toàn bộ Open Questions từ lần audit v1.0 đã được làm rõ chi tiết ở phiên bản SRS v2.0).*

---

## 📋 Unified Gap & Question Report

**Answered Questions:**

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *UI Danh sách vs Bộ lọc* | Trên màn hình Danh sách, có 1 thẻ tag Filter nằm ngang: `Tất cả` và `Đã xác minh`. Tuy nhiên, trong Popup "Bộ lọc tìm kiếm", **KHÔNG CÓ** tuỳ chọn lọc "Đã xác minh". Vậy thẻ `Đã xác minh` ở list là một nút Quick-filter (nhấn vào để lọc ngay lập tức) hay chỉ là text tĩnh báo hiệu? Nếu là Quick-filter, behavior của thanh ngang này thế nào (cuộn ngang)? | Thiếu đồng bộ giữa List UI và Modal Filter UI. Ảnh hưởng đến việc viết AC cho bộ lọc. | Resolved |
| Q2 | Medium | *Data Mapping (Nhu cầu)* | Ngoài List card, nhu cầu kết nối hiển thị tag rất ngắn (VD: `Đang tìm: Nhà phân phối`). Trong khi ở Màn hình chi tiết, mục Nhu cầu là 1 đoạn text dài (VD: `Tìm kiếm đại lý phân phối cấp 1 toàn quốc...`). Hệ thống Client lấy tag ngắn này ở đâu? (API cấp thêm 1 trường `shortNeedTag` hay Client phải tự xử lý cắt chữ?). | Đảm bảo tính nhất quán dữ liệu giữa màn danh sách và chi tiết. Cắt chữ sai có thể làm mất nghĩa. | Resolved |
| Q3 | Medium | *Hiển thị Sản phẩm/Dịch vụ* | Trong Hồ sơ công ty, danh sách Tag "Sản phẩm / Dịch vụ chính" có giới hạn số lượng hiển thị tối đa không? (VD công ty có 50 sản phẩm thì có hiện nút "Xem thêm" hay cuộn xuống vô tận?). | Tránh vỡ layout UI nếu số lượng Tag trả về từ API quá lớn. | Resolved |
| Q4 | Low | *Exception Handling (Missing Data)* | Trong phần "Thông tin liên hệ" ở Hồ sơ, nếu công ty đó chưa cập nhật Email hoặc Website thì UI sẽ xử lý thế nào? (Ẩn luôn cả dòng chữ đó đi, hay hiển thị chữ xám "Đang cập nhật" và disable hành động bấm mở App?). | Cần quy định rõ Empty State của từng field liên hệ. | Resolved |

**Open Questions:**
- *Không có. Toàn bộ câu hỏi đã được giải quyết.*

---

## 🟢 What's Good
- Áp dụng đầy đủ và chuẩn xác các rule CMR phức tạp (Debounce tìm kiếm, Lazy load list 20 items, Fallback avatar text).
- Cơ chế gọi OS Intent được định nghĩa chặt chẽ (đặc biệt là mailto:// và web browser), đảm bảo không nhầm lẫn với việc mở in-app webview.
- Cấu trúc "Hồ sơ công ty" phân rã theo 3 Section cực kỳ dễ hiểu, map đúng với các highlight box.
- **Tại phiên bản v2.0, spec đã được bao phủ hoàn hảo. Tất cả kịch bản UI liên đới đều được update cẩn thận.**

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- **Sẵn sàng 100% để thiết kế Test Case.**
- Tìm kiếm Textbox (Debounce 3s và Trim khoảng trắng tự động).
- Chức năng Dropdown đa điều kiện của Bộ lọc ở Bottom Sheet.
- Tính năng Quick-filter `Đã xác minh` hoạt động độc lập (cập nhật list ngay khi tap).
- UI List: Lazy load (có tự retry 3 lần), pull to refresh, empty state, logic fallback ảnh Avatar.
- Detail UI: Giới hạn "Xem thêm" nếu thẻ Sản phẩm vượt quá 3 dòng.
- Thao tác call OS Intent mở Browser/Mail app, xác nhận nút bị Disable và hiển thị `-` khi data rỗng.

**What CANNOT be tested yet (blocked by gaps):**
- *(Không có, mọi thứ đã rất tường minh)*

**Suggested test focus areas:**
- UI Boundary Test: Các doanh nghiệp có tên siêu dài hoặc địa chỉ siêu dài (kiểm tra text wrap ở thẻ Card và Detail).
- Data mapping: Đảm bảo nhãn "Đang tìm" ngoài list map 1-1 với Dropdown chuẩn.
- Interaction logic: Thử click đồng thời nút xem chi tiết ở 2 thẻ cùng lúc để check rule Debounce chống double-tap.
- Toggle Quick-filter: Trạng thái chọn cùng lúc nhiều tiêu chí trong Bottom Sheet kết hợp thao tác bật tắt Quick-filter `Đã xác minh` bên ngoài.

---

## 📌 Summary & Recommendation
Tài liệu SRS UC62 phiên bản v2.0 hoàn toàn đạt chuẩn đánh giá với số điểm **100.0/100 (READY)**. BA đã update tài liệu với các thông tin chuẩn xác (Quick-filter Đã xác minh, map thẻ Đang tìm với Dropdown, giới hạn "Xem thêm" cho Sản phẩm dài, và disable data lỗi). Đội QA có thể bắt đầu quá trình Test Design ngay hôm nay.

---

## 🔄 Changelog (Re-Audit)
- **12/05/2026 (Re-Audit v2):**
  - Thực hiện đánh giá lại file `UC62_tra-cuu-doanh-nghiep_srs_20260512_v2.md`.
  - Ghi nhận BA đã giải quyết hoàn chỉnh 4 Gaps từ đợt audit trước:
    - **UI Danh sách vs Bộ lọc:** Khẳng định thẻ `Đã xác minh` là nút Quick-filter gọi API lập tức (giải quyết Q1).
    - **Data Mapping Nhu cầu:** Xác nhận nhãn "Đang tìm" lấy tên gốc từ bảng Dropdown hệ thống (giải quyết Q2).
    - **Sản phẩm / Dịch vụ:** Bổ sung cơ chế gom nhóm và nút "Xem thêm" nếu vượt quá 3 dòng hiển thị (giải quyết Q3).
    - **Empty State Liên hệ:** Xác nhận điền ký tự `-` và chặn tap đối với link Email/Web nếu data bị rỗng (giải quyết Q4).
  - Tăng điểm các Knowledge Area từ ⚡ sang ✅, nâng tổng điểm lên mức **100/100**. Chuyển trạng thái thành **READY**.
