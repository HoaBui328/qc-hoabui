# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC58_tra-cuu-thuc-tuc-dau-tu_srs_20260512_v3.md`

---

## Feature Brief
Chức năng cho phép nhà đầu tư tìm kiếm, lọc (theo Lĩnh vực, Cấp thực hiện, Mức độ, Thời gian) và tra cứu thông tin chi tiết về các thủ tục đầu tư. Hệ thống hiển thị dưới dạng 3 tab: Thông tin chung (với các khối Highlight thông số), Trình tự thực hiện (Timeline), và Thành phần hồ sơ (Bắt buộc/Tùy chọn).

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

*(Lưu ý: Các open questions từ lần audit trước đã được BA cập nhật và làm rõ trong tài liệu SRS v3.0).*

---

## 📋 Unified Gap & Question Report

**Answered Questions:**

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | Medium | *Tab Thông tin chung -> Block Căn cứ pháp lý* | Tap vào các dòng Căn cứ pháp lý (VD: Luật Đầu tư 2020) có mở ra màn hình chi tiết văn bản, link trình duyệt, hay chỉ hiển thị text tĩnh thông thường? | QA cần biết để viết test case verify link điều hướng nếu có. | Resolved |
| Q2 | Medium | *Tab Trình tự thực hiện -> Timeline* | Khi phần mô tả hành động của một bước (Timeline nội dung) quá dài, hệ thống có tự động hiển thị `...` kèm nút "Xem thêm", hay đẩy layout dài vô tận? | Đảm bảo tính toàn vẹn của UI khi API trả về text siêu dài (Edge case Group A). | Resolved |
| Q3 | Low | *Ngôn ngữ (CMR-17)* | Khi người dùng đổi ngôn ngữ hệ thống, setting ngôn ngữ này được lưu tại Local Storage của máy hay được sync qua API? | Cần thiết để tester test logic persistence ngôn ngữ sau khi cài đặt lại app. | Resolved |

**Open Questions:**
- *Không có. Toàn bộ câu hỏi đã được giải quyết.*

---

## 🟢 What's Good
- Tài liệu cực kỳ chi tiết, tuân thủ tuyệt đối chuẩn định dạng 7 cột và các CMR rule.
- Đã cover toàn bộ các flow edge case: Debounce, Lazy load tự retry 3 lần, State Persistence.
- Đã kịp thời lược bỏ nút "Nộp hồ sơ" để đảm bảo đúng scope Tra cứu.
- AC và Logic lỗi được định nghĩa rõ ràng, cụ thể.
- **Tài liệu v3.0 đã giải quyết 100% các câu hỏi được đặt ra từ lần audit trước (Q1, Q2, Q3) rất chi tiết.**

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- **Toàn bộ chức năng đã sẵn sàng để thiết kế Test Case.**
- Toàn bộ luồng danh sách, tìm kiếm (debounce 3s), lọc dữ liệu (bao gồm rule Date Picker của CMR-15).
- Các thao tác UI: Swipe đổi tab, Lazy load, Skeleton, State Persistence khi back ra.
- Hiển thị data: Các badge thông số, danh sách hồ sơ bắt buộc/tùy chọn, format tiền tệ.
- Giao diện đặc thù: Căn cứ pháp lý tĩnh không tương tác, Timeline cuộn nội dung tự giãn dài vô tận.

**What CANNOT be tested yet (blocked by gaps):**
- *(Không có, tất cả các luồng đều đã được làm rõ)*

**Suggested test focus areas:**
- Happy path: Xem chi tiết 3 tab.
- Filter Boundary: Test case "Từ ngày lớn hơn Đến ngày" sẽ bị chặn.
- Đa ngôn ngữ UI: Chuyển đổi ngôn ngữ máy xem label tĩnh (Ví dụ: "Thành phần hồ sơ") có đổi tức thì không, kiểm tra đồng bộ lên hệ thống qua API.
- Căn cứ pháp lý: Xác nhận không có hành vi điều hướng (mở link) khi tap vào danh sách luật.
- Timeline Content: Mock dữ liệu description cực dài để kiểm tra việc giãn layout dọc liên tục mà không vỡ UI.
- Partial Failure API: Chặn thử API ở Tab 2 xem Tab 1 và 3 có render bình thường không (CMR-07).

---

## 📌 Summary & Recommendation
Tài liệu SRS UC58 phiên bản v3.0 đã hoàn thiện xuất sắc và đạt điểm **100.0/100 (READY)**. Phía BA đã giải đáp và bổ sung đầy đủ vào spec các kịch bản còn bỏ ngỏ ở lần đánh giá v2.0 (Hành vi text tĩnh Căn cứ pháp lý, nguyên lý hiển thị Timeline dài vô tận, đồng bộ đa ngôn ngữ qua API). Đội QA có thể bắt đầu thực hiện thiết kế Test Scenario và Test Case ngay lập tức. 

---

## 🔄 Changelog (Re-Audit)
- **12/05/2026 (Re-Audit v2):**
  - Thực hiện Re-audit trên file `UC58_tra-cuu-thuc-tuc-dau-tu_srs_20260512_v3.md`.
  - Phân tích và ghi nhận các nội dung giải đáp từ BA đã được cập nhật vào spec:
    - **Rule 1:** Căn cứ pháp lý chỉ là danh sách hiển thị tĩnh (giải quyết Q1).
    - **Rule 2:** Timeline hỗ trợ cuộn dọc tự giãn dòng vô tận không giới hạn ký tự (giải quyết Q2).
    - **Rule 3:** Setting đa ngôn ngữ được lưu và đồng bộ qua API (giải quyết Q3).
  - Cập nhật điểm các Knowledge Area số 5, 6, 7 lên full điểm (✅ Complete).
  - Chuyển toàn bộ câu hỏi (Q1, Q2, Q3) vào danh sách "Answered Questions".
  - Nâng điểm tổng từ `89.0` lên `100.0`. Chuyển trạng thái Readiness Verdict thành **READY**.
