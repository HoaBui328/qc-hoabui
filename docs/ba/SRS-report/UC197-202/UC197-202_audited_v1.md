# Báo cáo Audit Sự sẵn sàng của Yêu cầu (Readiness Review Report)

> **Dự án:** MBFS
> **Phân hệ:** Quản lý đầu tư ra nước ngoài
> **Feature/UC:** UC197-202 - Báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn (Mẫu I.19)
> **Người thực hiện:** QA Agent
> **Ngày audit:** 2026-05-11
> **Phiên bản tài liệu gốc:** 1.1

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
**Đánh giá:** ⚡ Partial (13/20)
- ✅ Các validate cơ bản được định nghĩa: Email, SĐT, định dạng Mã số thuế, giá trị Tổng số tiền cho vay (>0, 2 chữ số thập phân).
- ✅ Các trường tự điền từ Profile/ICR được định nghĩa Disabled/Enabled tùy theo kết quả API theo CMR_12.
- ⚠️ Thiếu validate max length cho trường "Tổng số tiền cho vay" (độ lớn tối đa của số tiền).
- ⚠️ Thiếu định dạng hiển thị tường minh của "Ngày cấp CCCD / CNĐKDN" — nên ghi rõ dd/MM/yyyy và validate ngày tối thiểu.
- ⚠️ Thiếu nội dung thông báo lỗi cụ thể khi Mã số thuế sai định dạng (chỉ ghi "Lỗi inline" nhưng không có text lỗi).
- ⚠️ Trường "Tên nhà đầu tư" không ghi Max length tường minh (CMR_06 default 500 ký tự nhưng UC không nhắc).
- ⚠️ Hành vi vượt max length của các trường Textbox/Textarea chưa được mô tả (block ký tự hay hiển thị warning?).
- ⚠️ Chưa rõ khi màn hình Chỉnh sửa, các field ICR đang Disabled có thể unlock để override không.

## 6. Functional Logic & Workflow Decomposition (Logic chức năng & Phân rã luồng)
**Đánh giá:** ⚡ Partial (13/20)
- ✅ Luồng Lập báo cáo, Xem, Sửa, Nộp, Xóa tuân thủ các CF (CF_01, CF_03, CF_04, CF_05, CF_07, CF_08, CF_09).
- ✅ Giao diện danh sách tuân thủ CS_02 đối với báo cáo không định kỳ.
- ⚠️ **[Mâu thuẫn #1]** UC ghi "Phân trang theo bản ghi. Tham chiếu: CMR_10" nhưng CS_02 (cập nhật 2026-05-11) quy định báo cáo không định kỳ dùng **Scroll dọc** khi >10 bản ghi, không dùng phân trang. Hai tài liệu mâu thuẫn trực tiếp.
- ⚠️ **[Mâu thuẫn #2]** Placeholder ô Search Mã báo cáo ghi là `"Nhập dữ liệu"` — mâu thuẫn với CS_01 (cập nhật 2026-05-11) quy định chuẩn là `"Tìm kiếm theo Mã báo cáo"`.
- ⚠️ **[Mâu thuẫn #3]** Empty State khi không tìm thấy ghi `"Không tìm thấy kết quả"` nhưng CS_02 quy định phải là `"Không tìm thấy dữ liệu phù hợp"` kèm hình minh họa.
- ⚠️ Luồng Nộp báo cáo: Theo CMR_03, chưa làm rõ quy trình Mẫu I.19 là 2 bước hay nhiều bước (trạng thái sau Submit: "Đã tiếp nhận" hay "Chờ duyệt").
- ⚠️ Nút [Nộp] từ Danh sách (CF_09): Khi validate FAIL, CF_09 redirect sang màn hình Chỉnh sửa — UC không đề cập hành vi này, có thể gây nhầm lẫn khi viết test.
- ⚠️ Chưa mô tả hành vi cụ thể khi nhấn [Tạo mới] và đã tồn tại nhiều báo cáo trước đó (không có giới hạn số lượng báo cáo tạo mới hay sao?).

## 7. Functional Integration Analysis (Phân tích tích hợp chức năng)
**Đánh giá:** ✅ Clear (10/10)
- ✅ Tích hợp API ICR lấy thông tin pháp lý của NĐT (CCCD/CNĐKDN, MST, Địa chỉ...).
- ✅ Tích hợp lấy dữ liệu Profile NĐT (Tên, Email, SĐT).

## 8. Acceptance Criteria (Tiêu chí nghiệm thu)
**Đánh giá:** ⚠️ Missing (0/10) - Đã tự sinh AC.
Tài liệu gốc không có phần Tiêu chí nghiệm thu rõ ràng. Dưới đây là AC được hệ thống tự động tổng hợp:

**AC1: Xem danh sách báo cáo**
- **Given** NĐT đăng nhập thành công.
- **When** Truy cập danh sách báo cáo Mẫu I.19.
- **Then** Chỉ hiển thị các báo cáo do NĐT đó tự lập. Danh sách hiển thị phẳng, sắp xếp mới nhất lên trên. Nút "Tạo mới" luôn hiển thị.

**AC2: Lập báo cáo - Autofill dữ liệu**
- **Given** NĐT nhấn Tạo mới.
- **When** Màn hình tạo mới mở ra.
- **Then** Tên, Email, SĐT tự động điền từ Profile (Enabled). Giấy tờ pháp lý, Địa chỉ, MST tự động gọi API ICR. Nếu ICR trả về dữ liệu -> field Disabled. Nếu không -> field Enabled.

**AC3: Lập báo cáo - Validate Conditional Required**
- **Given** NĐT đang ở form Tạo mới báo cáo.
- **When** Đối tượng là Tổ chức.
- **Then** Trường "Đại diện theo pháp luật" hiển thị dấu * bắt buộc. Nếu điền trường này -> trường "Chức vụ" cũng bắt buộc.
- **When** Đối tượng là Cá nhân.
- **Then** Trường "Đại diện theo pháp luật" không bắt buộc.

**AC4: Luồng nộp báo cáo**
- **Given** NĐT điền đầy đủ các thông tin bắt buộc và hợp lệ.
- **When** Nấn nút Nộp báo cáo.
- **Then** Hiển thị popup xác nhận P01. Sau khi đồng ý, bản ghi chuyển sang trạng thái tương ứng và hiển thị Toast T02.

## 9. Non-functional Requirements (Yêu cầu phi chức năng)
**Đánh giá:** ⚡ Partial (3/5)
- Không có mô tả tường minh ngoài quy tắc Debounce time cho thanh Search (từ CMR). Khuyến nghị bổ sung NFR về hiệu năng gọi API ICR.

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 5/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 13/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 13/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 0/10 | ⚠️ |
| 10| Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **79/110 → 71.8/100** | |

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|---------|
| Q1 | High | N/A (Missing) | Khi báo cáo Mẫu I.19 được nộp, trạng thái tiếp theo là "Chờ duyệt" hay "Đã tiếp nhận"? Quy trình phê duyệt nội bộ gồm 2 hay nhiều bước (per CMR_03)? | Không thể viết expected result chính xác cho luồng Submit. Mọi test case Submit sẽ bị block. | Open |
| Q2 | High | UC197-202.1 mục 3: "Phân trang theo bản ghi. Tham chiếu: CMR_10" / CS_02 (2026-05-11): "Scroll dọc nếu >10 bản ghi" | **Mâu thuẫn:** UC tham chiếu CMR_10 (phân trang), nhưng CS_02 (cập nhật 2026-05-11) quy định báo cáo không định kỳ dùng Scroll dọc thay vì phân trang. Tài liệu nào đúng? | Gây mâu thuẫn khi verify UI — phân trang và scroll là 2 hành vi hoàn toàn khác nhau. | Open |
| Q3 | High | UC197-202.1 mục 2: Placeholder Search bar = `"Nhập dữ liệu"` / CS_01 (2026-05-11): Placeholder = `"Tìm kiếm theo Mã báo cáo"` | **Mâu thuẫn:** Placeholder ô tìm kiếm trong UC khác chuẩn CS_01 mới nhất. Tài liệu nào đúng? | QA không thể xác định expected text chính xác khi verify UI. | Open |
| Q4 | High | UC197-202.1 mục 2: "Nếu không tìm thấy: hiển thị màn hình trắng với text `Không tìm thấy kết quả`" / CS_02: `"Không tìm thấy dữ liệu phù hợp"` kèm hình minh họa | **Mâu thuẫn:** Empty state text và UI (màn hình trắng vs có hình minh họa) không khớp giữa UC và CS_02. | QA không thể xác định expected result đúng cho test case empty state. | Open |
| Q5 | High | UC197-202.2 mục 2: Trường "Mã số thuế" — "Lỗi inline nếu sai định dạng" | Thiếu nội dung thông báo lỗi inline khi MST sai định dạng (chỉ ghi "lỗi inline" chung chung, không có text cụ thể). BA cần bổ sung text lỗi. | Không có expected message → không thể verify thông báo lỗi. | Open |
| Q6 | Medium | UC197-202.2 mục 2: Trường số 11 "Tổng số tiền cho vay (USD)" | Có giới hạn max value không? Nhập số âm (nếu dùng dấu trừ) thì sao — CMR_05 cho phép dấu trừ mặc định nhưng UC ghi validate "> 0"? Hành vi chặn ký tự `-` có bị block ngay khi nhập không? | Cần xác định để viết test case boundary và negative cho trường số tiền. | Open |
| Q7 | Medium | UC197-202.2 mục 2: Trường "Tên nhà đầu tư" — Tham chiếu CMR_06, không ghi max length | Trường "Tên nhà đầu tư" không ghi max length tường minh. CMR_06 default 500 ký tự — xác nhận áp dụng 500 ký tự không? | QA không có giá trị boundary để test. | Open |
| Q8 | Medium | UC197-202.2 mục 3: Trường "Ngày cấp CCCD/CNĐKDN" — Validate ≤ ngày hôm nay | Có validate ngày tối thiểu không (ví dụ: ngày 01/01/1900 có bị reject không)? Định dạng hiển thị trong field là dd/MM/yyyy hay MM/dd/yyyy? | Thiếu boundary tối thiểu và format rõ ràng → không thể viết test case boundary cho trường ngày. | Open |
| Q9 | Medium | UC197-202.3 mục 2: Nút [Nộp] từ Danh sách — Tham chiếu CF_09 | Theo CF_09, khi validate FAIL từ màn hình Danh sách, hệ thống sẽ **redirect sang màn hình Chỉnh sửa** và hiển thị lỗi inline. UC không đề cập hành vi này — xác nhận UC197-202 áp dụng đúng theo CF_09? | QA cần biết expected redirect để viết test case Nộp-thất bại từ danh sách. | Open |
| Q10 | Medium | UC197-202.2 mục 3 — Màn hình Chỉnh sửa (CF_03) | Khi mở màn hình Chỉnh sửa, các field ICR đang Disabled (API đã trả dữ liệu trước đó), NĐT có thể unlock/override để chỉnh sửa không? Hay luôn Disabled trong suốt vòng đời bản ghi? | Hành vi này ảnh hưởng trực tiếp đến test case chỉnh sửa sau khi tạo. | Open |
| Q11 | Low | N/A (Missing) | Có giới hạn số lượng báo cáo I.19 tối đa một NĐT có thể tạo không (không định kỳ → có thể tạo vô hạn)? | Cần xác định để test edge case tạo nhiều bản ghi. | Open |
| Q12 | Low | UC197-202.2: Nhóm trường max length (mục 10–20) | Hành vi khi nhập vượt max length là gì — block ký tự ngay khi gõ (hard limit) hay hiển thị warning sau khi submit? | CMR_06 không mô tả hành vi vượt max length → không thể verify UX tại boundary. | Open |
| Q13 | Low | N/A (Missing) | Metadata "Cơ quan nhận: Bộ Tài chính / Ngân hàng Nhà nước" — người dùng có cần chọn cơ quan nhận hay đây là thông tin cố định hệ thống tự gắn vào báo cáo? | Nếu cần chọn thì phải có UI element, nếu cố định thì không cần test. | Open |
| Q14 | Low | UC197-202.2 — Trường "Đại diện theo pháp luật" và "Chức vụ" | Đối với tài khoản Cá nhân, các trường này có thể có dữ liệu từ API ICR không? Nếu ICR trả dữ liệu → trường Disabled dù Optional? Và khi trường 6 Disabled (có dữ liệu ICR) thì trường 7 có tự động Required không? | Hành vi phức tạp của conditional required kết hợp Disabled/Enabled cần rõ ràng để test đúng. | Open |

---

### 🟢 What's Good
- Tài liệu định nghĩa rõ quy tắc phân quyền độc lập cho NĐT (không dùng chung bản ghi, không áp dụng CMR_01/CMR_02).
- Xác định rõ tính chất báo cáo không định kỳ và kiến trúc giao diện danh sách tương ứng (CS_02).
- Đã link đầy đủ các tài liệu Common Functions (CF) và Common Business Rules (CMR).
- Logic Conditional Required (Đại diện theo pháp luật / Chức vụ) được mô tả tương đối rõ.
- Đầy đủ placeholder và max length cho hầu hết các trường khoản vay.

### 🧪 Testability Outlook
**What CAN be tested now:**
- Autofill dữ liệu từ Profile (Tên, Email, SĐT) và logic Enabled luôn.
- Validate Email, SĐT format.
- Validate MST (10 hoặc 13 chữ số) — chỉ thiếu error message text.
- Luồng Lưu nháp, Xem PDF Preview, Xuất báo cáo (.docx), In, Xóa (khi chưa nộp).
- Conditional Required: Đại diện PL bắt buộc khi Tổ chức; Chức vụ bắt buộc khi mục 6 có giá trị.
- CMR_12: ICR trả dữ liệu → Disabled; ICR null → Enabled; ICR timeout → Toast T05 + Enabled.

**What CANNOT be tested yet (blocked by gaps):**
- Trạng thái sau Submit (Q1 — High blocker).
- UI danh sách: phân trang vs scroll (Q2 — mâu thuẫn).
- Placeholder và empty state text chính xác (Q3, Q4 — mâu thuẫn).
- Hành vi Nộp từ danh sách khi validate fail (Q9).
- Override field ICR Disabled trong màn hình Chỉnh sửa (Q10).

**Suggested test focus areas** *(once gaps are resolved)*:
- Happy path: Autofill ICR thành công → Điền khoản vay → Nộp báo cáo → Verify trạng thái.
- Alternative: Lưu nháp → Thoát → Quay lại Chỉnh sửa → Nộp từ màn hình Danh sách.
- Boundary & validation: Max length các textarea, số tiền > 0, ngày cấp ≤ hôm nay.
- Error & exception: API ICR timeout, sai định dạng Email/SĐT/MST, để trống trường bắt buộc.
- UI-specific: Phân trang/Scroll danh sách, empty state, placeholder text.

### 📌 Summary & Recommendation
Tài liệu UC197-202 có nền tảng tốt về phân quyền và cấu trúc form. Tuy nhiên có **3 mâu thuẫn trực tiếp** giữa UC và CMR/CS (phân trang, placeholder, empty state) cần BA xác nhận ưu tiên tài liệu nào. Ngoài ra thiếu thông tin trạng thái sau Submit và một số chi tiết validate. **Recommendation: CONDITIONALLY READY** — QA có thể test các luồng cơ bản (Lưu nháp, Validate form, Xuất báo cáo), nhưng **chưa thể test luồng Submit và verify UI danh sách** cho đến khi BA giải đáp Q1–Q4.
