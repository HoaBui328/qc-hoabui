# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC59_tra-cuu-bao-cao-dau-tu_srs_20260512_v2.md` (phiên bản v2.1)

---

## Feature Brief
Chức năng cho phép người dùng public tra cứu thông tin Báo cáo đầu tư. Giao diện bao gồm danh sách báo cáo, bộ lọc tìm kiếm theo nhiều tiêu chí, thanh Tab nhóm lĩnh vực báo cáo và màn hình chi tiết hiển thị số liệu nổi bật, tóm tắt nội dung cùng mục lục báo cáo. Chức năng cũng tích hợp màn hình "Thông tin cơ quan" (hiển thị profile cơ quan và liên kết đến các thủ tục, tài liệu liên quan thông qua Tab Bar).

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

---

## 📋 Unified Gap & Question Report

**Answered Questions:**

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *Màn hình Chi tiết báo cáo* | Trên màn hình Chi tiết báo cáo có hiển thị "48 trang" và "Mục lục chính", nhưng **không thấy có nút "Tải tài liệu" (Download) hay "Xem toàn văn" (View PDF)**. Đây là thiếu sót thiết kế (Design missing) hay do logic nghiệp vụ chỉ cho xem tóm tắt và mục lục? | Đây là chức năng tra cứu cốt lõi của người dùng. Thiếu tính năng xem nội dung gốc sẽ ảnh hưởng lớn đến trải nghiệm. | Resolved |
| Q2 | Medium | *Chi tiết báo cáo -> Mục lục* | Tap vào các dòng trong mục "Mục lục chính" (VD: "Tr. 4") thì chỉ xem text tĩnh hay hệ thống có tự động mở màn hình đọc PDF nhảy tới đúng trang số 4? | QA cần verify behavior tương tác của các dòng list này. | Resolved |
| Q3 | Medium | *Thông tin cơ quan -> Tab Tài liệu* | Dropdown sắp xếp "Mới nhất >" ở góc phải màn hình Tab Tài liệu phát hành khi tap vào sẽ gồm những lựa chọn nào? (VD: Cũ nhất, Tên A-Z, Lượt xem nhiều nhất?). | Thiếu option để QA viết test case kiểm tra sắp xếp (Sorting). | Resolved |
| Q4 | Low | *Thông tin cơ quan -> Gọi OS Intent* | Khi thực hiện thao tác Gọi điện, Website, Bản đồ... nếu thiết bị báo lỗi không thể mở App (VD: Máy tính bảng không hỗ trợ SIM, hoặc chưa cài Google Maps), App sẽ hiển thị Toast báo lỗi cụ thể như thế nào? | Đảm bảo xử lý triệt để Exception Handling của luồng Mobile App. | Resolved |
| Q5 | Medium | *Mục 2.1 - Trường 1 (Nút Quay lại, Tiêu đề & Icon thông báo)* | Đã bổ sung "Icon thông báo (hình chuông) ở góc phải" nhưng chưa định nghĩa hành động (Quy tắc hành động). Tap vào icon này hệ thống sẽ làm gì (VD: mở màn hình danh sách thông báo)? | QA cần biết chính xác flow điều hướng của nút này để thiết kế test case chuyển màn hình. | Resolved |

**Open Questions:**

- *(Không có. Toàn bộ câu hỏi đã được giải quyết.)*

---

## 🟢 What's Good
- Đã cập nhật layout và thẻ thông tin bám sát thiết kế UI mới nhất, các thành phần đều rõ ràng (Tab Lĩnh vực, thanh đếm số lượng báo cáo, hiển thị đa sắc PDF).
- Định nghĩa rõ logic đồng bộ giữa thanh Tab Group ngoài màn hình và Dropdown Lĩnh vực trong Bottom Sheet, giúp QA dễ dàng lên scenario kiểm tra tính nhất quán.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- **Chức năng cơ bản đã sẵn sàng 99% để viết Test Case.**
- Logic đồng bộ filter Tab Lĩnh vực và Dropdown.
- Giao diện thẻ báo cáo mới với đầy đủ thông tin (cơ quan, ngày, trang).
- Mọi chức năng khác đã được clear từ v2.0 (Lazy load, Pull to Refresh, PDF Viewer, OS Intent).

**What CANNOT be tested yet (blocked by gaps):**
- *(Không có, tất cả các luồng đều đã rõ ràng)*

**Suggested test focus areas:**
- UI-specific checks: Xác minh hiển thị thẻ báo cáo đúng thiết kế (icon có đa dạng màu sắc không, các hashtag).
- Boundary & validation tests: Kiểm tra việc filter liên hoàn giữa text search, bộ lọc dropdown và tab lĩnh vực.
- Integration: Đảm bảo chọn tab "FDI" ở ngoài thì khi mở bộ lọc lên, dropdown "Lĩnh vực" tự động chọn "FDI", và ngược lại.

---

## 📌 Summary & Recommendation
SRS UC59 phiên bản mới nhất (v2.2) đạt **100.0/100 (READY)**. BA đã cập nhật đầy đủ cấu trúc UI theo màn hình mới, bổ sung đồng bộ Tab Lĩnh vực và Dropdown, đồng thời cũng đã cập nhật thêm quy tắc chuyển màn hình cho Icon Thông báo trên Header. Đội QA có thể tiến hành tạo Test Scenarios/Test Cases ngay.

---

## 🔄 Changelog (Re-Audit)
- **12/05/2026 (Re-Audit v2):** (Lịch sử đợt trước) Giải quyết các câu hỏi về PDF, Fallback OS Intent. Điểm: 100.0/100.
- **13/05/2026 (Re-Audit v3):**
  - Thực hiện đánh giá lại dựa trên thay đổi giao diện ở phiên bản `v2.1`.
  - Ghi nhận tài liệu bổ sung Tab Lĩnh vực, Thanh đếm số lượng, Cập nhật Card báo cáo và logic đồng bộ Tab/Dropdown rất tốt.
  - Sau khi phát hiện thiếu mô tả hành động cho `Icon Thông báo` ở Header (Q5), BA đã lập tức bổ sung rule vào bản `v2.2`.
  - Tổng điểm cập nhật thành `100.0/100`. Kết luận: **READY**.
