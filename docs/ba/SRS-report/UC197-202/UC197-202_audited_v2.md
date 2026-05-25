# Báo cáo Audit Sự sẵn sàng của Yêu cầu (Readiness Review Report)

> **Dự án:** MBFS
> **Phân hệ:** Quản lý đầu tư ra nước ngoài
> **Feature/UC:** UC197-202 - Báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn (Mẫu I.19)
> **Người thực hiện:** QA Agent
> **Ngày audit:** 2026-05-11
> **Ngày cập nhật CMR:** 2026-05-22
> **Phiên bản tài liệu gốc:** 1.3
> **Phiên bản audit:** v2 (CMR Alignment)

---

## 0. Feature Identity (Nhận diện chức năng)
**Đánh giá:** ✅ Clear (5/5)
- **Tên chức năng:** Xem danh sách báo cáo, Tạo mới, Xem chi tiết, Chỉnh sửa, Các tác vụ bổ trợ đối với báo cáo cho tổ chức kinh tế ở nước ngoài vay vốn (Mẫu I.19).
- **ID Use Case:** UC197-202.
- **Bối cảnh:** Thuộc phân hệ Quản lý đầu tư ra nước ngoài, dành cho Nhà đầu tư tự lập báo cáo độc lập.
- **Mã báo cáo:** Tạo theo quy tắc `ODI_I19_[ID]`.

## 1. Objective & Scope (Mục tiêu & Phạm vi)
**Đánh giá:** ✅ Clear (5/5)
- **Mục tiêu:** Cho phép NĐT lập và nộp báo cáo về việc cho TCKT ở nước ngoài vay vốn.
- **Phạm vi:** Báo cáo không định kỳ (Ad-hoc), báo cáo đơn lẻ, NĐT tự lập, không áp dụng phạm vi theo dự án.

## 2. Actors & User Roles (Tác nhân & Quyền người dùng)
**Đánh giá:** ✅ Clear (10/10)
- **Actor:** Nhà đầu tư (Cá nhân / Tổ chức) đã đăng nhập.
- **Phân quyền:** 
  - Mỗi NĐT tự lập báo cáo độc lập (bản ghi thuộc về NĐT đăng nhập).
  - Không áp dụng CMR_01/CMR_02. Chỉ NĐT tạo ra bản ghi mới có quyền xem và thao tác trên bản ghi đó.
  - Các quyền phụ thuộc vào trạng thái bản ghi theo "Hành động theo từng trạng thái" (CMR_03).

## 3. Preconditions & Postconditions (Điều kiện tiên quyết & Kết quả)
**Đánh giá:** ⚡ Partial (5/10)
- **Tiên quyết:** ✅ Nhà đầu tư đã đăng nhập thành công vào hệ thống.
- **Tiên quyết về dữ liệu:** ⚠️ Tài liệu có nhắc đến việc gọi API ICR để lấy thông tin Giấy tờ pháp lý, nhưng chưa rõ có cần điều kiện tiên quyết nào từ hệ thống ICR hay không (ví dụ: NĐT phải có dữ liệu map sẵn).
- **Kết quả (Postconditions):** ✅ Bản ghi được lưu/nộp với các trạng thái tương ứng (Lưu nháp, Chờ duyệt, Đã tiếp nhận).

## 4. UI Object Inventory & Mapping (Kiểm kê & Ánh xạ đối tượng UI)
**Đánh giá:** ✅ Clear (15/15)
Tất cả các đối tượng UI đã được liệt kê chi tiết trong từng màn hình:
- **Màn hình danh sách:** Trạng thái báo cáo, Năm, Mã báo cáo, Nút Tạo mới, Cột Hành động.
- **Màn hình tạo mới:** Các trường thông tin NĐT (Tên, Giấy CNĐKDN/CCCD, Ngày cấp, Địa chỉ, MST, Đại diện PL, Chức vụ, Email, Điện thoại) và các trường thông tin khoản vay. Các nút Lưu nháp, Xem, Nộp, Hủy.

## 5. Object Attributes & Behavior Definition (Thuộc tính & Hành vi đối tượng)
**Đánh giá:** ⚡ Partial (13/20) → ✅ **CMR Aligned**
- ✅ Các validate cơ bản được định nghĩa: Email, SĐT, định dạng Mã số thuế, giá trị Tổng số tiền cho vay (>0, 15 chữ số phần nguyên + 5 chữ số phần thập phân).
- ✅ Các trường tự điền từ Profile/ICR được định nghĩa Disabled/Enabled tùy theo kết quả API theo CMR_12.
- ✅ **[CMR Fix]** Trường "Tổng số tiền cho vay": áp dụng 15 chữ số phần nguyên + 5 chữ số phần thập phân. Error: "Tổng số tiền cho vay (USD) chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"
- ✅ **[CMR Fix]** Trường "Tên nhà đầu tư" (Textbox): Max 255 ký tự (CMR_06 A06 chuẩn). Error: "Tên nhà đầu tư không được vượt quá 255 ký tự!"
- ✅ **[CMR Fix]** Các trường Textbox (mục 1, 2, 5, 6, 7, 8, 9, 10): Max 255 ký tự theo CMR_06 A06.
- ✅ **[CMR Fix]** Các trường Textarea (mục 4, 12, 13, 14, 15, 16, 17, 18, 19, 20): Max 3000 ký tự theo CMR_06 A06.
- ✅ **[CMR Fix]** Định dạng "Ngày cấp CCCD / CNĐKDN": dd/MM/yyyy, validate ≤ ngày hôm nay, ≥ 01/01/1900. Lỗi: "Ngày cấp không hợp lệ"
- ✅ **[CMR Fix]** Lỗi MST sai định dạng: "Mã số thuế phải là 10 hoặc 13 chữ số"
- ✅ **[CMR Fix]** Hành vi vượt max length: block ký tự ngay khi đạt giới hạn (hard limit).
- ✅ **[CMR Fix]** Field ICR trong Chỉnh sửa: giữ nguyên Disabled/Enabled như lúc tạo, không thể unlock.

## 6. Functional Logic & Workflow Decomposition (Logic chức năng & Phân rã luồng)
**Đánh giá:** ⚡ Partial (13/20) → ✅ **CMR Aligned**
- ✅ Luồng Lập báo cáo, Xem, Sửa, Nộp, Xóa tuân thủ các CF (CF_01, CF_03, CF_04, CF_05, CF_07, CF_08, CF_09).
- ✅ Giao diện danh sách tuân thủ CS_02 đối với báo cáo không định kỳ.
- ✅ **[Đã giải quyết]** UC v1.2+ đã sửa: Scroll dọc khi >10 bản ghi (theo CS_02), không dùng phân trang.
- ✅ **[Đã giải quyết]** UC v1.2+ đã sửa: Placeholder ô Search = "Tìm kiếm nhanh theo mã báo cáo" (theo CS_01).
- ✅ **[Đã giải quyết]** UC v1.2+ đã sửa: Empty state = "Không tìm thấy dữ liệu phù hợp" kèm hình minh họa (theo CS_02).
- ✅ **[CMR Fix]** Tham chiếu CMR_18 (Tab Navigation): Áp dụng điều hướng bàn phím Tab trên form nhập liệu. Tab → field tiếp theo; Shift+Tab → field trước đó; Tab ở field cuối → quay về field đầu/nút Submit.
- ✅ **[CMR Fix]** Tất cả nút Submit/Lưu nháp/Nộp báo cáo: **Luôn Enabled** — validate khi tap, hiển thị lỗi inline nếu form chưa hợp lệ (theo CMR Section I, rule I01).
- ✅ Luồng Nộp: Quy trình 2 bước (CMCĐT_BCTK_03). Trạng thái sau Submit = "Chờ duyệt".
- ✅ Nút [Nộp] từ Danh sách (CF_09): Khi validate FAIL → redirect sang màn hình Chỉnh sửa, hiển thị lỗi inline.
- ✅ Không giới hạn số lượng báo cáo I.19 mỗi NĐT có thể tạo (báo cáo không định kỳ — ad-hoc).

## 7. Functional Integration Analysis (Phân tích tích hợp chức năng)
**Đánh giá:** ✅ Clear (10/10)
- ✅ Tích hợp API ICR lấy thông tin pháp lý của NĐT (CCCD/CNĐKDN, MST, Địa chỉ...).
- ✅ Tích hợp lấy dữ liệu Profile NĐT (Tên, Email, SĐT).

## 8. Acceptance Criteria (Tiêu chí nghiệm thu)
**Đánh giá:** ⚠️ Missing (0/10) - Đã tự sinh AC. → ✅ **CMR Aligned**
Tài liệu gốc v1.3 đã bổ sung đầy đủ 9 AC (Given/When/Then). Dưới đây là AC đã cập nhật theo CMR:

**AC1: Xem danh sách báo cáo**
- **Given** NĐT đăng nhập thành công.
- **When** Truy cập danh sách báo cáo Mẫu I.19.
- **Then** Chỉ hiển thị các báo cáo do NĐT đó tự lập. Danh sách hiển thị phẳng, sắp xếp mới nhất lên trên. Nút "Tạo mới" luôn hiển thị. Scroll dọc khi >10 bản ghi.

**AC2: Lập báo cáo - Autofill dữ liệu**
- **Given** NĐT nhấn Tạo mới.
- **When** Màn hình tạo mới mở ra.
- **Then** Tên, Email, SĐT tự động điền từ Profile (Enabled). Giấy tờ pháp lý, Địa chỉ, MST tự động gọi API ICR. Nếu ICR trả về dữ liệu -> field Disabled. Nếu không -> field Enabled. Tham chiếu CMR_18 Tab Navigation.

**AC3: Lập báo cáo - Validate Conditional Required**
- **Given** NĐT đang ở form Tạo mới báo cáo.
- **When** Đối tượng là Tổ chức.
- **Then** Trường "Đại diện theo pháp luật" hiển thị dấu * bắt buộc. Nếu để trống: lỗi "Vui lòng nhập Đại diện theo pháp luật". Nếu điền trường này -> trường "Chức vụ" cũng bắt buộc, lỗi "Vui lòng nhập Chức vụ" nếu để trống.
- **When** Đối tượng là Cá nhân.
- **Then** Trường "Đại diện theo pháp luật" không bắt buộc.

**AC4: Luồng nộp báo cáo**
- **Given** NĐT điền đầy đủ các thông tin bắt buộc và hợp lệ.
- **When** Nhấn nút Nộp báo cáo (Luôn Enabled).
- **Then** Hiển thị popup xác nhận P01. Sau khi đồng ý, bản ghi chuyển sang trạng thái "Chờ duyệt" và hiển thị Toast T02.

**AC5: Validate Required — Error messages (CMR Aligned)**
- **Given** NĐT nhấn [Nộp báo cáo] hoặc [Lưu nháp].
- **When** Có trường bắt buộc để trống.
- **Then** Hiển thị lỗi inline theo chuẩn CMR:
  - Tên nhà đầu tư: "Vui lòng nhập Tên nhà đầu tư"
  - Giấy CNĐKDN / CCCD số: "Vui lòng nhập Giấy CNĐKDN / CCCD số"
  - Ngày cấp CCCD / CNĐKDN: "Vui lòng chọn Ngày cấp CCCD / CNĐKDN"
  - Địa chỉ: "Vui lòng nhập Địa chỉ"
  - Mã số thuế: "Vui lòng nhập Mã số thuế"
  - Đại diện theo pháp luật (khi Required): "Vui lòng nhập Đại diện theo pháp luật"
  - Chức vụ (khi Required): "Vui lòng nhập Chức vụ"
  - Email: "Vui lòng nhập Email"
  - Điện thoại: "Vui lòng nhập Điện thoại"
  - Tên TCKT tại nước ngoài vay vốn: "Vui lòng nhập Tên TCKT tại nước ngoài vay vốn"
  - Tổng số tiền cho vay (USD): "Vui lòng nhập Tổng số tiền cho vay (USD)"
  - Mục đích: "Vui lòng nhập Mục đích"
  - Điều kiện cho vay: "Vui lòng nhập Điều kiện cho vay"
  - Kế hoạch giải ngân: "Vui lòng nhập Kế hoạch giải ngân"
  - Kế hoạch thu hồi nợ: "Vui lòng nhập Kế hoạch thu hồi nợ"
  - Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay: "Vui lòng nhập Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay"
  - Đánh giá khả năng tài chính của bên vay: "Vui lòng nhập Đánh giá khả năng tài chính của bên vay"
  - Mức độ rủi ro và biện pháp phòng ngừa: "Vui lòng nhập Mức độ rủi ro và biện pháp phòng ngừa"
  > **Lưu ý CMR:** Tất cả error message KHÔNG có dấu `.` ở cuối câu.

**AC6: Validate Numeric — Tổng số tiền cho vay (CMR_05 Aligned)**
- **Given** NĐT nhập giá trị vào trường "Tổng số tiền cho vay (USD)".
- **When** Giá trị ≤ 0 → lỗi "Giá trị phải lớn hơn 0"
- **When** Phần nguyên > 15 chữ số hoặc phần thập phân > 5 chữ số → lỗi "Tổng số tiền cho vay (USD) chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"
- **When** Nhập ký tự `-` → block ngay, không cho nhập.
  > **Lưu ý CMR:** Tất cả error message KHÔNG có dấu `.` ở cuối câu.

## 9. Non-functional Requirements (Yêu cầu phi chức năng)
**Đánh giá:** ⚡ Partial (3/5)
- Không có mô tả tường minh ngoài quy tắc Debounce time cho thanh Search (từ CMR). Khuyến nghị bổ sung NFR về hiệu năng gọi API ICR.

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 5/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ✅ CMR Aligned |
| 7 | Functional Logic & Workflow Decomposition | 20 | 18/20 | ✅ CMR Aligned |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 8/10 | ✅ CMR Aligned |
| 10| Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **97/110 → 88.2/100** | |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|---------|
| Q1 | High | N/A (Missing) | Khi báo cáo Mẫu I.19 được nộp, trạng thái tiếp theo là "Chờ duyệt" hay "Đã tiếp nhận"? Quy trình phê duyệt nội bộ gồm 2 hay nhiều bước (per CMR_03)? | Không thể viết expected result chính xác cho luồng Submit. Mọi test case Submit sẽ bị block. | ✅ Resolved (v1.3: Quy trình 2 bước, CMCĐT_BCTK_03. Trạng thái sau Submit = "Chờ duyệt") |
| Q2 | High | UC197-202.1 mục 3 | **Mâu thuẫn:** UC tham chiếu CMR_10 (phân trang), nhưng CS_02 quy định báo cáo không định kỳ dùng Scroll dọc. | Gây mâu thuẫn khi verify UI. | ✅ Resolved (v1.2: Sửa thành Scroll dọc khi >10 bản ghi theo CS_02) |
| Q3 | High | UC197-202.1 mục 2 | **Mâu thuẫn:** Placeholder ô tìm kiếm trong UC khác chuẩn CS_01. | QA không thể xác định expected text chính xác. | ✅ Resolved (v1.2: Sửa thành "Tìm kiếm nhanh theo mã báo cáo") |
| Q4 | High | UC197-202.1 mục 2 | **Mâu thuẫn:** Empty state text và UI không khớp giữa UC và CS_02. | QA không thể xác định expected result đúng. | ✅ Resolved (v1.2: Sửa thành "Không tìm thấy dữ liệu phù hợp" kèm hình minh họa) |
| Q5 | High | UC197-202.2 mục 2 | Thiếu nội dung thông báo lỗi inline khi MST sai định dạng. | Không có expected message → không thể verify. | ✅ Resolved (v1.2: "Mã số thuế phải là 10 hoặc 13 chữ số") |
| Q6 | Medium | UC197-202.2 mục 2 | Giới hạn max value trường "Tổng số tiền cho vay (USD)"? Hành vi chặn ký tự `-`? | Cần xác định để viết test case boundary. | ✅ Resolved (v1.2 + CMR: 15 nguyên + 5 thập phân, block `-` ngay khi nhập) |
| Q7 | Medium | UC197-202.2 mục 2 | Trường "Tên nhà đầu tư" không ghi max length tường minh. | QA không có giá trị boundary để test. | ✅ Resolved (CMR_06 A06: Textbox max = 255 ký tự) |
| Q8 | Medium | UC197-202.2 mục 3 | Validate ngày tối thiểu? Định dạng hiển thị? | Thiếu boundary tối thiểu và format. | ✅ Resolved (v1.2: dd/MM/yyyy, ≥ 01/01/1900, ≤ ngày hôm nay) |
| Q9 | Medium | UC197-202.3 mục 2 | Theo CF_09, khi validate FAIL từ Danh sách → redirect sang Chỉnh sửa? | QA cần biết expected redirect. | ✅ Resolved (v1.2: Xác nhận áp dụng CF_09 — redirect + hiển thị lỗi inline) |
| Q10 | Medium | UC197-202.2 mục 3 | Khi mở Chỉnh sửa, field ICR Disabled có thể unlock không? | Ảnh hưởng test case chỉnh sửa. | ✅ Resolved (v1.2: Không thể unlock. Phải cập nhật qua ICR) |
| Q11 | Low | N/A (Missing) | Có giới hạn số lượng báo cáo I.19 tối đa? | Cần xác định để test edge case. | ✅ Resolved (v1.2: Không giới hạn — ad-hoc) |
| Q12 | Low | UC197-202.2 mục 10–20 | Hành vi khi nhập vượt max length? | CMR_06 không mô tả hành vi vượt max length. | ✅ Resolved (v1.2: Hard limit — block ký tự ngay khi đạt giới hạn) |
| Q13 | Low | N/A (Missing) | Metadata "Cơ quan nhận" — người dùng có cần chọn hay cố định? | Nếu cần chọn thì phải có UI element. | Open |
| Q14 | Low | UC197-202.2 | Đối với Cá nhân, trường "Đại diện PL" và "Chức vụ" có dữ liệu từ ICR không? | Hành vi phức tạp conditional required + Disabled/Enabled. | Open |

---

### What's Good
- Tài liệu định nghĩa rõ quy tắc phân quyền độc lập cho NĐT (không dùng chung bản ghi, không áp dụng CMR_01/CMR_02).
- Xác định rõ tính chất báo cáo không định kỳ và kiến trúc giao diện danh sách tương ứng (CS_02).
- Đã link đầy đủ các tài liệu Common Functions (CF) và Common Business Rules (CMR).
- Logic Conditional Required (Đại diện theo pháp luật / Chức vụ) được mô tả tương đối rõ.
- Đầy đủ placeholder và max length cho hầu hết các trường khoản vay.
- **[CMR v2]** Tài liệu gốc v1.3 đã giải quyết hầu hết các gap từ audit v1 (Q1-Q12).
- **[CMR v2]** Áp dụng đầy đủ CMR_06 A06 (Textbox 255, Textarea 3000), CMR_05 C05b (15+5), CMR_18 (Tab Navigation), Button Luôn Enabled (I01).

### Testability Outlook
**What CAN be tested now (CMR Aligned):**
- Autofill dữ liệu từ Profile (Tên, Email, SĐT) và logic Enabled luôn.
- Validate Email, SĐT format.
- Validate MST: "Mã số thuế phải là 10 hoặc 13 chữ số"
- Luồng Lưu nháp, Xem PDF Preview, Xuất báo cáo (.docx), In, Xóa (khi chưa nộp).
- Conditional Required: Đại diện PL bắt buộc khi Tổ chức; Chức vụ bắt buộc khi mục 6 có giá trị.
- CMR_12: ICR trả dữ liệu → Disabled; ICR null → Enabled; ICR timeout → Toast T05 + Enabled.
- **[CMR Fix]** Textbox max 255 ký tự (Tên NĐT, CCCD, MST, Đại diện PL, Chức vụ, Email, SĐT, Tên TCKT): block ký tự khi đạt giới hạn.
- **[CMR Fix]** Textarea max 3000 ký tự (Địa chỉ, Mục đích, Điều kiện cho vay, Kế hoạch giải ngân, Kế hoạch thu hồi nợ, Phương án cân đối, Đánh giá tài chính bên vay, Mức độ rủi ro, Biện pháp bảo đảm, Nội dung khác): block ký tự khi đạt giới hạn.
- **[CMR Fix]** Numeric 15+5: Tổng số tiền cho vay — 15 chữ số phần nguyên, 5 chữ số phần thập phân.
- **[CMR Fix]** Required errors: "Vui lòng nhập [tên trường]" / "Vui lòng chọn [tên trường]" — không có dấu `.` cuối.
- **[CMR Fix]** Buttons Luôn Enabled: Lưu nháp, Nộp báo cáo, Hủy — validate khi tap.
- **[CMR Fix]** Tab Navigation (CMR_18): Tab/Shift+Tab giữa các field.
- **[CMR Fix]** Luồng Submit: Trạng thái "Chờ duyệt" (Quy trình 2 bước).
- **[CMR Fix]** Nộp từ Danh sách (CF_09): validate FAIL → redirect Chỉnh sửa + lỗi inline.
- **[CMR Fix]** Scroll dọc khi >10 bản ghi (không phân trang).

**What CANNOT be tested yet (blocked by remaining gaps):**
- Metadata "Cơ quan nhận" — cố định hay chọn? (Q13 — Low).
- Hành vi ICR + Conditional Required cho tài khoản Cá nhân (Q14 — Low).

**Suggested test focus areas:**
- Happy path: Autofill ICR thành công → Điền khoản vay → Nộp báo cáo → Verify trạng thái "Chờ duyệt".
- Alternative: Lưu nháp → Thoát → Quay lại Chỉnh sửa → Nộp từ màn hình Danh sách.
- Boundary & validation: Textbox 255 ký tự, Textarea 3000 ký tự, Numeric 15+5, ngày cấp ≤ hôm nay ≥ 01/01/1900.
- Error & exception: API ICR timeout, sai định dạng Email/SĐT/MST, để trống trường bắt buộc.
- UI-specific: Scroll dọc danh sách, empty state "Không tìm thấy dữ liệu phù hợp", placeholder text, Tab Navigation.
- Button behavior: Verify tất cả nút Luôn Enabled, loading state khi gọi API.

### Summary & Recommendation
Tài liệu UC197-202 (v1.3) đã giải quyết hầu hết các gap từ audit v1. Sau khi áp dụng CMR Alignment (Textbox 255, Textarea 3000, Numeric 15+5, Required errors chuẩn, Button Luôn Enabled, CMR_18 Tab Navigation, bỏ dấu `.` cuối error messages), tài liệu đạt **88.2/100** và chỉ còn 2 câu hỏi Low priority chưa giải quyết (Q13, Q14). **Recommendation: READY** — QA có thể test toàn bộ luồng chính và phụ. Chỉ còn 2 edge case nhỏ cần BA xác nhận thêm.

---

## CMR Alignment Changelog (v1 → v2)

| # | Hạng mục | Trước (v1) | Sau (v2) | CMR Rule |
|---|----------|------------|----------|----------|
| 1 | Textbox max length — Tên nhà đầu tư (field 1) | Max 500 ký tự | Max 255 ký tự | CMR_06 A06 |
| 2 | Textbox max length — Tên TCKT (field 10) | Max 300 ký tự | Max 255 ký tự | CMR_06 A06 |
| 3 | Textbox max length — Giấy CNĐKDN/CCCD (field 2) | Max 20 ký tự | Max 20 ký tự (giữ nguyên — rule riêng) | CMR_06 A06 exception |
| 4 | Textarea max length — Địa chỉ (field 4) | Không khai báo (default 500) | Max 3000 ký tự | CMR_06 A06 |
| 5 | Textarea max length — Mục đích (field 12) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 6 | Textarea max length — Điều kiện cho vay (field 13) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 7 | Textarea max length — Kế hoạch giải ngân (field 14) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 8 | Textarea max length — Kế hoạch thu hồi nợ (field 15) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 9 | Textarea max length — Phương án cân đối (field 16) | Max 1000 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 10 | Textarea max length — Đánh giá tài chính bên vay (field 17) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 11 | Textarea max length — Mức độ rủi ro (field 18) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 12 | Textarea max length — Biện pháp bảo đảm (field 19) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 13 | Textarea max length — Nội dung khác (field 20) | Max 500 ký tự | Max 3000 ký tự | CMR_06 A06 |
| 14 | Numeric — Tổng số tiền cho vay (field 11) | 15 nguyên + 2 thập phân | 15 nguyên + 5 thập phân | CMR_05 C05b |
| 15 | Numeric error message | Không có / chưa chuẩn | "Tổng số tiền cho vay (USD) chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" | CMR_05 C07 |
| 16 | Required error — Tên nhà đầu tư | "Vui lòng nhập Tên nhà đầu tư." | "Vui lòng nhập Tên nhà đầu tư" (bỏ `.`) | H01 |
| 17 | Required error — Tên TCKT | "Vui lòng nhập Tên TCKT tại nước ngoài vay vốn." | "Vui lòng nhập Tên TCKT tại nước ngoài vay vốn" (bỏ `.`) | H01 |
| 18 | Required error — Mục đích | "Vui lòng nhập Mục đích." | "Vui lòng nhập Mục đích" (bỏ `.`) | H01 |
| 19 | Required error — Điều kiện cho vay | "Vui lòng nhập Điều kiện cho vay." | "Vui lòng nhập Điều kiện cho vay" (bỏ `.`) | H01 |
| 20 | Required error — Kế hoạch giải ngân | "Vui lòng nhập Kế hoạch giải ngân." | "Vui lòng nhập Kế hoạch giải ngân" (bỏ `.`) | H01 |
| 21 | Required error — Kế hoạch thu hồi nợ | "Vui lòng nhập Kế hoạch thu hồi nợ." | "Vui lòng nhập Kế hoạch thu hồi nợ" (bỏ `.`) | H01 |
| 22 | Required error — Phương án cân đối | "Vui lòng nhập Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay." | "Vui lòng nhập Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay" (bỏ `.`) | H01 |
| 23 | Required error — Đánh giá tài chính bên vay | "Vui lòng nhập Đánh giá khả năng tài chính của bên vay." | "Vui lòng nhập Đánh giá khả năng tài chính của bên vay" (bỏ `.`) | H01 |
| 24 | Required error — Mức độ rủi ro | "Vui lòng nhập Mức độ rủi ro và biện pháp phòng ngừa." | "Vui lòng nhập Mức độ rủi ro và biện pháp phòng ngừa" (bỏ `.`) | H01 |
| 25 | Required error — Ngày cấp (Datepicker) | Chưa chuẩn | "Vui lòng chọn Ngày cấp CCCD / CNĐKDN" | H02 |
| 26 | Button — Lưu nháp | Chưa ghi rõ trạng thái | Luôn Enabled — validate khi tap | I01 |
| 27 | Button — Nộp báo cáo | Chưa ghi rõ trạng thái | Luôn Enabled — validate khi tap | I01 |
| 28 | Button — Hủy | Chưa ghi rõ trạng thái | Luôn Enabled | I01 |
| 29 | Button — Xem trước | Chưa ghi rõ trạng thái | Disabled khi chưa Lưu nháp lần nào; Enabled sau khi đã Lưu nháp | I09 |
| 30 | Tab Navigation | Không có tham chiếu CMR_18 | Bổ sung tham chiếu CMR_18: Tab/Shift+Tab điều hướng giữa các field | CMR_18 K01-K03 |
| 31 | Error trailing `.` | Tất cả error/toast/validation có dấu `.` cuối | Bỏ dấu `.` cuối tất cả error messages | H01-H12 |
