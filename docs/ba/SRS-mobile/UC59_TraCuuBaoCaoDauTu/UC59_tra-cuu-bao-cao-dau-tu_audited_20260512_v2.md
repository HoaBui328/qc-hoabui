# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC59_tra-cuu-bao-cao-dau-tu_srs_20260512_v2.md`

---

## Feature Brief
Chức năng cho phép người dùng public tra cứu thông tin Báo cáo đầu tư. Giao diện bao gồm danh sách báo cáo, bộ lọc tìm kiếm theo nhiều tiêu chí, và màn hình chi tiết hiển thị số liệu nổi bật, tóm tắt nội dung cùng mục lục báo cáo. Chức năng cũng tích hợp màn hình "Thông tin cơ quan" (hiển thị profile cơ quan và liên kết đến các thủ tục, tài liệu liên quan thông qua Tab Bar).

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

*(Lưu ý: Các Open Questions từ đợt audit trước đã được BA cập nhật và làm rõ trong tài liệu SRS v2.0).*

---

## 📋 Unified Gap & Question Report

**Answered Questions:**

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *Màn hình Chi tiết báo cáo* | Trên màn hình Chi tiết báo cáo có hiển thị "48 trang" và "Mục lục chính", nhưng **không thấy có nút "Tải tài liệu" (Download) hay "Xem toàn văn" (View PDF)**. Đây là thiếu sót thiết kế (Design missing) hay do logic nghiệp vụ chỉ cho xem tóm tắt và mục lục? | Đây là chức năng tra cứu cốt lõi của người dùng. Thiếu tính năng xem nội dung gốc sẽ ảnh hưởng lớn đến trải nghiệm. | Resolved |
| Q2 | Medium | *Chi tiết báo cáo -> Mục lục* | Tap vào các dòng trong mục "Mục lục chính" (VD: "Tr. 4") thì chỉ xem text tĩnh hay hệ thống có tự động mở màn hình đọc PDF nhảy tới đúng trang số 4? | QA cần verify behavior tương tác của các dòng list này. | Resolved |
| Q3 | Medium | *Thông tin cơ quan -> Tab Tài liệu* | Dropdown sắp xếp "Mới nhất >" ở góc phải màn hình Tab Tài liệu phát hành khi tap vào sẽ gồm những lựa chọn nào? (VD: Cũ nhất, Tên A-Z, Lượt xem nhiều nhất?). | Thiếu option để QA viết test case kiểm tra sắp xếp (Sorting). | Resolved |
| Q4 | Low | *Thông tin cơ quan -> Gọi OS Intent* | Khi thực hiện thao tác Gọi điện, Website, Bản đồ... nếu thiết bị báo lỗi không thể mở App (VD: Máy tính bảng không hỗ trợ SIM, hoặc chưa cài Google Maps), App sẽ hiển thị Toast báo lỗi cụ thể như thế nào? | Đảm bảo xử lý triệt để Exception Handling của luồng Mobile App. | Resolved |

**Open Questions:**
- *Không có. Toàn bộ câu hỏi đã được giải quyết.*

---

## 🟢 What's Good
- Cấu trúc SRS trình bày xuất sắc, rõ ràng các block thông tin, layout hiển thị 3 cột số liệu động có `%` tăng trưởng.
- Quy chiếu toàn vẹn đến các luật CMR (Debounce, Lazy load riêng biệt giữa các Tab, Partial API Failure).
- Khung sườn đa màn hình phức tạp (Chi tiết kết nối đến màn Thông tin cơ quan độc lập) được xử lý liên kết mạch lạc.
- **Tài liệu v2.0 đã giải quyết 100% các câu hỏi (Q1-Q4) từ lần audit trước, đưa ra các kịch bản fallback rõ ràng.**

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- **Toàn bộ chức năng đã sẵn sàng để thiết kế Test Case.**
- Luồng xem danh sách, cuộn lazy load, thực hiện pull to refresh.
- Hoạt động của Bottom Sheet bộ lọc (nhất là trường hợp Dropdown chọn "Năm phát hành").
- Format màu sắc/hiển thị của % tăng trưởng (Xanh lá có dấu `+` và đỏ có dấu `-`).
- Điều hướng swipe tab ở Màn hình cơ quan ban hành.
- Chức năng đọc file PDF: Click Mục lục để view PDF và test logic nhảy đúng số trang tương ứng.
- Hoạt động của Dropdown sắp xếp Mới nhất/Cũ nhất tại tab Tài liệu.
- Behavior gọi các Intent của OS (Gọi điện, Trình duyệt, Maps) và các kịch bản fallback (VD: iOS không có Google Maps fallback sang Apple Maps).

**What CANNOT be tested yet (blocked by gaps):**
- *(Không có, tất cả các luồng đều đã rõ ràng)*

**Suggested test focus areas:**
- Boundary Test: Tỷ lệ phần trăm có số quá lớn, định dạng tiền tệ khi string siêu dài (Ví dụ: 15.000.000.000.000 tỷ VNĐ).
- Hardware API Test: Các nút Gọi, Maps trên thiết bị vật lý thật (iOS vs Android), đặc biệt là test kịch bản không có SIM (gọi điện) và không có Google Maps (chỉ đường trên iOS).
- Chức năng PDF Viewer: Test khả năng nhảy trang chính xác khi tap vào từng mục trong Mục lục chính.

---

## 📌 Summary & Recommendation
SRS UC59 v2.0 đạt **100.0/100 (READY)**. BA đã phản hồi chi tiết các Gaps bằng cách bổ sung quy tắc tương tác Mục lục để đọc file PDF, làm rõ tính năng sort tài liệu, cũng như bổ sung cơ chế fallback rất chặt chẽ khi gọi OS Intent. Đội QA có thể bắt đầu làm việc thiết kế Test Scenario/Test Case ngay.

---

## 🔄 Changelog (Re-Audit)
- **12/05/2026 (Re-Audit v2):**
  - Thực hiện đánh giá lại dựa trên `UC59_tra-cuu-bao-cao-dau-tu_srs_20260512_v2.md`.
  - Xác nhận BA đã cập nhật đầy đủ logic giải đáp thắc mắc:
    - **Logic mở PDF:** Không có nút "Xem toàn văn", user sẽ tap vào từng dòng "Mục lục chính" để mở PDF Viewer và nhảy trực tiếp đến trang đó (giải quyết Q1, Q2).
    - **Sort:** Dropdown ở Tab Tài liệu có 2 tùy chọn "Mới nhất", "Cũ nhất" (giải quyết Q3).
    - **Exception OS Intent:** Bổ sung fallback gọi Apple Maps nếu máy iOS thiếu Google Maps, màn hình Dialer vẫn mở nhận số khi máy không có SIM (giải quyết Q4).
  - Nâng toàn bộ điểm của các khu vực 5, 6, 7, 8, 9 lên mức tối đa.
  - Tổng điểm cập nhật thành `100.0/100`. Kết luận: **READY**.
