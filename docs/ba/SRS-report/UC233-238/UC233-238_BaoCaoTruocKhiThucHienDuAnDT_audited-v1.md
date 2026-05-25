# UC Readiness Review — UC233-238

| Thuộc tính         | Giá trị                                                    |
| -------------------- | ------------------------------------------------------------ |
| **UC**             | UC233-238: Báo cáo trước khi thực hiện dự án đầu tư     |
| **Phiên bản UC**  | 1.0                                                          |
| **Ngày audit**     | 2026-05-21                                                   |
| **Auditor**        | QC Agent (BA-audit-SRS-report)                               |
| **Nguồn tham chiếu** | CMR_01–CMR_18, CF_01–CF_09, CS_01–CS_02                |

---

## 1. Audit Summary

| # | Knowledge Area                        | Score | Max | Ghi chú                                                  |
| - | --------------------------------------- | ----- | --- | ---------------------------------------------------------- |
| 1 | Functional Completeness                 | 10    | 15  | Thiếu mapping UC chi tiết, thiếu mô tả Phạm vi dự án |
| 2 | UI/UX Specification                     | 11    | 15  | Đầy đủ field table, thiếu empty state cho Phần I/II    |
| 3 | Business Rules & Validation             | 10    | 12  | Validation Email/ĐT có, thiếu validate Đơn vị tiếp nhận |
| 4 | State & Workflow Management             | 10    | 12  | CMR_03 tham chiếu đúng, luồng 2 bước rõ ràng           |
| 5 | Error Handling & Messages               | 8     | 10  | Toast/inline có qua CF, thiếu edge case API fail NĐT    |
| 6 | Integration & Data Flow                 | 7     | 10  | API NĐT mô tả, thiếu endpoint/contract cụ thể         |
| 7 | Permission & Access Control             | 10    | 10  | CMR_01 áp dụng đúng, phân quyền rõ ràng                |
| 8 | Non-Functional Requirements             | 3     | 8   | Không đề cập performance, concurrent access              |
| 9 | Traceability & Consistency              | 8     | 10  | UC mapping có, tham chiếu CMR/CF đầy đủ                 |
| 10| Documentation Quality                   | 7     | 8   | Cấu trúc chuẩn, changelog có, thiếu Mapping chi tiết   |

**Tổng điểm: 84 / 110 → Normalized: 76 / 100**

**Verdict: CONDITIONALLY READY**

---

## 2. Unified Gap & Question Report

| ID    | Loại     | Mục ảnh hưởng              | Mô tả                                                                                                                                                                                                  | Mức độ   | Đề xuất                                                                                                    |
| ----- | --------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| GAP-01 | Gap       | UC233-238.1 Mục 1            | Thiếu bảng **Mapping chi tiết** (UC nào → chức năng nào) giống UC035-040. Hiện chỉ ghi "Chức năng đáp ứng usecase số: 233-238" mà không liệt kê chi tiết từng UC.                                | Medium    | Bổ sung bảng mapping: UC233=Lập+Lưu nháp+Nộp, UC234=Xem+Lọc+Xuất+Nhập từ file, UC235=Chỉnh sửa, v.v. |
| GAP-02 | Gap       | UC233-238.1 Mục 2 (#1)      | Placeholder Search bar ghi "Tìm kiếm nhanh theo mã báo cáo" nhưng mô tả lại ghi tìm theo **Mã báo cáo** VÀ **Tên dự án**. Placeholder không khớp với phạm vi tìm kiếm thực tế.                | Low       | Đổi placeholder thành: "Tìm kiếm nhanh theo mã báo cáo, tên dự án" (theo CMR_06 STD-04b).                |
| GAP-03 | Gap       | UC233-238.1 Mục 2 (#2)      | Filter Năm thiếu tham chiếu **CMR_16** (option "Tất cả" mặc định cho filter dropdown).                                                                                                              | Low       | Bổ sung CMR_16 vào tham chiếu filter Năm.                                                                  |
| GAP-04 | Gap       | UC233-238.1 Mục 3            | Thiếu mô tả **Empty State** khi chưa có báo cáo nào (danh sách trống). CS_01 Mục 3 quy định phải có empty state.                                                                                    | Medium    | Bổ sung: "Empty state — chưa có báo cáo nào: hiển thị 'Chưa có báo cáo nào.'"                            |
| GAP-05 | Gap       | UC233-238.1 Mục 3            | Thiếu mô tả vị trí nút **[Lập báo cáo]** trên giao diện danh sách. CS_02 quy định nút hiển thị trên header.                                                                                       | Low       | Bổ sung: "Nút [Lập báo cáo] hiển thị trên header màn hình Danh sách."                                    |
| GAP-06 | Question  | UC233-238.2 Metadata         | Metadata ghi **Phạm vi dự án = "Không có"** nhưng Phần II có trường "Tên dự án đầu tư (dự kiến)" (#001). Vậy báo cáo này KHÔNG chọn dự án từ hệ thống mà NĐT tự nhập tên dự án dự kiến? | High      | BA xác nhận: Báo cáo này không có Phạm vi dữ liệu nguồn input (không chọn Dự án từ dropdown)?             |
| GAP-07 | Gap       | UC233-238.2 Mục 2 (#0)      | Trường "Đơn vị tiếp nhận" thiếu mô tả nguồn dữ liệu dropdown (danh sách cơ quan lấy từ đâu? API hay static list?).                                                                               | Medium    | Bổ sung nguồn dữ liệu cho dropdown Đơn vị tiếp nhận.                                                      |
| GAP-08 | Gap       | UC233-238.2 Mục 3            | Tham chiếu **CMR_18** (Tab Navigation) nhưng biểu mẫu này không có nhiều tab. CMR_18 có áp dụng cho form đơn trang không?                                                                           | Low       | BA xác nhận CMR_18 có áp dụng cho form single-page hay chỉ multi-tab.                                      |
| GAP-09 | Gap       | UC233-238.2 Mục 3            | Thiếu mô tả xử lý khi **API NĐT fail** (timeout/lỗi mạng). CMR_12 quy định trường chuyển Enabled khi API fail, nhưng NĐT Cá nhân (#2-9) và DN (#10-16) đều Disabled cố định → mâu thuẫn.    | High      | BA xác nhận: Khi API fail, các trường NĐT (#2-16) có chuyển Enabled hay giữ Disabled + hiển thị lỗi?      |
| GAP-10 | Gap       | UC233-238.2 Phần I           | Thiếu mô tả **nguồn API** để auto-fill thông tin NĐT. Khi thêm NĐT mới, hệ thống lấy thông tin từ đâu? Người dùng chọn NĐT từ dropdown trước rồi API fill, hay tự động theo dự án?            | High      | BA xác nhận luồng: Thêm NĐT → chọn NĐT từ danh sách → API fill thông tin?                                |
| GAP-11 | Gap       | UC233-238.2 Phần I (#17)    | Trường "Vốn điều lệ" thuộc block NĐT Doanh nghiệp nhưng không rõ: mỗi NĐT DN có 1 trường Vốn điều lệ riêng, hay chỉ có 1 trường chung cho toàn bộ báo cáo?                                   | Medium    | BA xác nhận scope trường Vốn điều lệ.                                                                       |
| GAP-12 | Gap       | UC233-238.3 Action Mapping   | Nút **Nhập từ file** (#8) có điều kiện "Chưa có hồ sơ hoặc hồ sơ ở trạng thái Lưu nháp / **Chờ duyệt** / Yêu cầu chỉnh sửa". Cho phép nhập từ file khi đã "Chờ duyệt" có hợp lý không? Bản ghi Chờ duyệt đã bị khóa theo CMR_03. | High      | BA xác nhận: Nhập từ file khi trạng thái "Chờ duyệt" có ghi đè bản ghi hiện tại không? Hay chỉ áp dụng khi chưa có hồ sơ? |
| GAP-13 | Gap       | UC233-238.2 Mục 2 (#010a)   | Trường "Tổng số lao động / Người VN / Người nước ngoài" gộp 3 giá trị vào 1 dòng. Không rõ đây là 1 trường hay 3 trường riêng biệt.                                                              | Medium    | BA xác nhận: Tách thành 3 trường riêng (Tổng, VN, Nước ngoài) hay 1 trường text tự do?                    |
| GAP-14 | Gap       | UC233-238 toàn bộ           | Thiếu mô tả **Mapping UC chi tiết** cho UC233-238.2 và UC233-238.3. UC035-040 gốc cũng không có mapping rõ ràng cho .2 và .3.                                                                       | Low       | Bổ sung mapping: UC233=?, UC234=?, UC235=Chỉnh sửa, UC236=Phê duyệt, UC237=Xem lịch sử, UC238=In.       |

---

## 3. What's Good

- Cấu trúc tài liệu tuân thủ chuẩn SRS template (3 child UC: .1 List, .2 Create, .3 Supplementary).
- Phân quyền rõ ràng, tham chiếu CMR_01 nhất quán.
- Validation Email và Điện thoại có regex pattern cụ thể, thời điểm validate rõ ràng.
- Dynamic Block NĐT và Conditional Block Nhà ở mô tả logic trigger/clear đầy đủ.
- Cascade delete 008c khi xóa giai đoạn có popup cảnh báo — edge case tốt.
- Action Mapping bảng UC233-238.3 đầy đủ 8 actions với điều kiện hiển thị và phân quyền.

---

## 4. Testability Outlook

| Khía cạnh                    | Đánh giá                                                                                     |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| Happy path testable?           | Có — luồng Lập → Lưu nháp → Nộp rõ ràng qua CF_01                                       |
| Negative/edge cases testable?  | Phần lớn — thiếu edge case API fail cho NĐT, thiếu empty state                            |
| Validation rules testable?     | Có — Email regex, ĐT regex, CMR_05/CMR_06 đều có message lỗi cụ thể                      |
| Permission matrix testable?    | Có — CMR_01 phân quyền TCKT vs NĐT rõ ràng                                                |
| State transitions testable?    | Có — CMR_03 + quy trình 2 bước                                                              |

---

## 5. Summary & Recommendation

**Verdict: CONDITIONALLY READY (76/100)**

Tài liệu UC233-238 có cấu trúc tốt, phân quyền rõ ràng, validation chi tiết. Tuy nhiên có **4 gaps mức High** cần BA giải đáp trước khi QA có thể thiết kế test cases đầy đủ:

1. **GAP-06**: Xác nhận Phạm vi dữ liệu nguồn input (không chọn Dự án?)
2. **GAP-09**: Xử lý khi API NĐT fail — mâu thuẫn với CMR_12
3. **GAP-10**: Luồng thêm NĐT mới — nguồn API nào?
4. **GAP-12**: Nhập từ file khi trạng thái "Chờ duyệt" — logic ghi đè?

Sau khi BA trả lời 4 câu hỏi trên, tài liệu có thể đạt **READY**.
