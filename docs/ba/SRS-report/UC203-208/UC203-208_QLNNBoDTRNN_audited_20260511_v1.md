# Readiness Review Report — UC203-208

- **Document:** UC203-208_QLNNBoDTRNN.md
- **Review Date:** 2026-05-11
- **Reviewer:** Agent
- **Version:** v1

---

## 📌 Summary & Recommendation

Tài liệu UC203-208 mô tả tương đối đầy đủ về phân quyền, trạng thái hiển thị cho báo cáo Mẫu II.4 trên Admin Site. Tuy nhiên, thiếu hoàn toàn Wireframe/Mockup khiến UI Object Inventory bị chặn (score 0/15 → auto-fail). Ngoài ra còn nhiều gap về validate, naming, luồng Import, và quy trình duyệt chưa được làm rõ.

**Verdict:** ❌ **NOT READY** — Cần bổ sung Mockup và phản hồi 17 câu hỏi trong backlog.

---

## 📊 Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|----------------|-----|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 0/15 | ⚠️ BLOCKED |
| 6 | Object Attributes & Behavior | 20 | 10/20 | ⚡ |
| 7 | Functional Logic & Workflow | 20 | 13/20 | ⚡ |
| 8 | Functional Integration | 10 | 5/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 0/5 | ⚠️ |
| **Total** | | **110** | **63** | **57.3/100** |

**Auto-fail:** Critical Area #5 = 0 (missing Design).

---

## 🔴 Blockers

- `[BLOCKED: UI Design / Wireframe not accessible]`: Không có file Mockup cho cả 3 màn hình (Danh sách, Lập báo cáo, Xem chi tiết).

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | N/A (Missing) | Bổ sung file Mockup/Wireframe cho UC203-208 (Danh sách, Lập báo cáo, Xem chi tiết). | Không thể map và kiểm tra layout, vị trí button, spacing, icon — Section 4/5 bị chặn hoàn toàn (score 0). | Open |
| Q2 | High | UC203-208.2 mục 3: "Nộp thành công: Chuyển trạng thái thành 'Đã tiếp nhận' hoặc 'Chờ duyệt' (theo CMR_03)" | Quy trình duyệt Mẫu II.4 là **2 bước** (Nộp → Đã tiếp nhận) hay **>2 bước** (Nộp → Chờ duyệt → Đã tiếp nhận)? Xác nhận chính xác 1 giá trị. | Tester không thể viết expected result cho luồng Nộp nếu không biết trạng thái đầu ra. Ảnh hưởng trực tiếp đến state machine test. | Open |
| Q3 | High | UC203-208.2 mục 12: Nút "Xem" | CF_01 gọi nút này là **[Xem chi tiết]** (PDF Preview Popup), nhưng UC gọi là **[Xem]**. Tên chính thức là gì? Ngoài ra, CF_07.1 cũng có nút [Xem] trên màn hình View — 2 nút này cùng tên gây nhầm lẫn. | Tester cần biết chính xác label hiển thị trên UI để viết test step. Nếu 2 nút cùng tên "Xem" trên 2 màn hình khác nhau sẽ gây nhầm lẫn khi báo bug. | Open |
| Q4 | Medium | UC203-208.2 mục 2: "Số văn bản — Textbox — Max 50 ký tự. Placeholder: 'VD: 123/2026/VB-BTC'" | Trường "Số văn bản" có áp dụng quy tắc CMR_13 (Số công văn) không? Ví dụ placeholder `123/2026/VB-BTC` có chứa năm `2026` — không khớp với pattern CMR_13 `[Số thứ tự]/[Ký hiệu 1]-[Ký hiệu 2]`. Nếu KHÔNG áp dụng CMR_13, thì validate format cụ thể là gì (hay chỉ cần max 50 ký tự)? | Xác định có cần test auto-uppercase, block ký tự, validate `/` và `-` theo CMR_13 hay không. Nếu không áp dụng, cần ghi rõ trường này là free-text. | Open |
| Q5 | Medium | UC203-208.2 mục 1: "Tên cơ quan — Tham chiếu CMR_12" | CMR_12 quy định trạng thái trường theo 4 case: (1) Trước khi gọi API → Disabled, (2) API trả data → Disabled, (3) API null → Enabled, (4) API lỗi → Toast T05 + Enabled. Tuy nhiên UC mô tả trường này **luôn Disabled**, auto-fill từ profile tổ chức. **Câu hỏi:** Trường này lấy data từ **API call** (áp dụng đúng CMR_12 bao gồm case null và lỗi) hay lấy từ **session/token** (luôn có sẵn, không cần gọi API)? Nếu lấy từ API, behavior khi API trả null hoặc lỗi là gì? | Test case cần biết: (a) có mock API không, (b) trường có khi nào Enabled cho nhập tay không, (c) có Toast T05 khi lỗi không. | Open |
| Q6 | Medium | UC203-208.1 mục 4: "Placeholder: 'Nhập dữ liệu'" | CS_01 Mục 3 quy định placeholder chuẩn cho Search bar là **"Tìm kiếm theo Mã báo cáo"**. UC lại ghi placeholder **"Nhập dữ liệu"**. Placeholder chính thức là gì? | Placeholder sai sẽ bị report lỗi UI khi test. Cần thống nhất. | Open |
| Q7 | Medium | UC203-208.1 mục 4: "Nhập liệu tự do tìm theo mã báo cáo (Live Search)" | CS_01 Mục 3 yêu cầu **Debounce time 300–500ms** cho Search bar. UC không đề cập debounce. Có áp dụng debounce theo CS_01 không? | Ảnh hưởng NFR: nếu không debounce, mỗi keystroke trigger 1 API call → performance issue. Tester cần biết để test timing. | Open |
| Q8 | Medium | UC203-208.1 mục 4: "Nếu không tìm thấy: hiển thị text 'Không tìm thấy kết quả'" | CS_01 Mục 3 quy định empty state là **"Không tìm thấy dữ liệu phù hợp"** kèm hình ảnh placeholder. UC lại ghi **"Không tìm thấy kết quả"** (không nhắc hình ảnh). Văn bản và hình ảnh minh họa chính thức là gì? | Test case cần đúng từng ký tự expected text. Thiếu/sai placeholder image cũng là lỗi UI. | Open |
| Q9 | Medium | UC203-208.1 mục 3: "Phân trang theo số kỳ hạn / trang. Tham chiếu: CMR_10." | CS_01 Mục 4 quy định **"Hiển thị tối đa 10 bản ghi trong mỗi kỳ hạn. Nếu vượt quá 10, kích hoạt scroll dọc bên trong riêng kỳ hạn đó"** (không dùng phân trang). UC lại tham chiếu CMR_10 (phân trang 10/20/50/100). Áp dụng rule nào: **scroll trong kỳ** (CS_01) hay **phân trang** (CMR_10)? | 2 rule mâu thuẫn — tester không biết test phân trang hay scroll. | Open |
| Q10 | Medium | UC203-208.2: Không đề cập CMR_14 | UC không nhắc đến CMR_14 (Dirty Form Guard) ở bất kỳ đâu. Theo CF_01 mục "Xử lý nút [Hủy]", khi form dirty phải hiển thị popup P02 *"Dữ liệu chưa được lưu"*. **Xác nhận:** Màn hình Lập báo cáo (CF_01) và Chỉnh sửa (CF_03) của UC này có áp dụng CMR_14 hay không? | Nếu áp dụng (đúng chuẩn CF_01), cần test popup cảnh báo khi Hủy/navigate khi form dirty. Nếu không, cần ghi rõ exception. | Open |
| Q11 | Medium | UC203-208.2 mục 9: "File đính kèm — Cho phép upload nhiều file" | **Giới hạn số lượng file tối đa** cho phép upload là bao nhiêu? Có giới hạn **tổng dung lượng** (total size) không? Có cho phép upload **file trùng tên** không? | Tester cần biết boundary: max file count, max total size, behavior khi upload file trùng tên. Thiếu spec này sẽ không test được edge case. | Open |
| Q12 | Medium | UC203-208.2 mục 9: Lỗi file đính kèm | UC mô tả lỗi inline *"Định dạng file không được hỗ trợ. Vui lòng sử dụng PDF, Excel hoặc Word"*. Tuy nhiên, bảng Toast (list-toast-messages.md) không có mã lỗi tương ứng cho file upload đặc thù của UC. **Xác nhận:** Lỗi file upload hiển thị dạng **inline error** bên dưới khu vực upload hay dạng **Alert trên popup** (như CF_02 A03)? | Vị trí hiển thị lỗi khác nhau → test step khác nhau. | Open |
| Q13 | Medium | UC203-208.1 mục 8: "Import — Tham chiếu CF_02" | UC có nút [Import] nhưng **không mô tả luồng Import chi tiết**. Báo cáo này "Không có phạm vi" → áp dụng **CF_02 Case 2** (không chọn Phạm vi, download template trắng, upload file). **Xác nhận:** (a) Có đúng áp dụng CF_02 Case 2? (b) Template import có format gì (.xlsx hay .docx)? (c) Tên file template theo quy tắc `Mau_[Mã-báo-cáo]_[YYYYMMDD]_[HHMM]` → cụ thể là `Mau_ODI_II4_[YYYYMMDD]_[HHMM]`? | Tester cần biết rõ luồng Import, template format, và file naming để test end-to-end. | Open |
| Q14 | Medium | UC203-208.3 mục 1 (Nộp): "Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_03" | CF_09 (Nộp từ Danh sách) Step 3b quy định: khi validate FAIL, hệ thống **mở màn hình Lập báo cáo** và hiển thị lỗi inline + scroll/focus vào lỗi đầu tiên. UC không mô tả behavior này. **Xác nhận:** Khi Nộp từ Danh sách mà validate fail, hệ thống có chuyển sang màn hình Lập/Chỉnh sửa và hiển thị lỗi theo CF_09 không? | Tester cần biết expected behavior khi Submit từ listing fail — redirect hay chỉ toast. | Open |
| Q15 | Medium | UC203-208.1 mục 1 (Yearpicker filter): "Giá trị mặc định: Năm hiện tại" | CS_01 Mục 2 quy định Yearpicker chỉ **Enable** các năm có data đã nộp hoặc năm tài chính hiện tại, các năm khác **Disabled**. UC không đề cập rule này. **Xác nhận:** Filter Yearpicker trên Danh sách có áp dụng rule Enable/Disable theo CS_01 không? | Nếu áp dụng, cần test: năm không có data → disabled. Nếu không, user có thể chọn năm bất kỳ. | Open |
| Q16 | Medium | UC203-208.3 — Export: "Kết xuất file .docx. Tham chiếu: CF_04" | CF_04 quy định tên file export cho báo cáo cơ quan: `[Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan-nộp]`. **Câu hỏi:** Mã cơ quan nộp lấy từ đâu (profile tổ chức?) và format cụ thể là gì? VD: `ODI-II4-1_nam-2026_BKHDT`? | Test case export cần verify tên file chính xác. Thiếu spec naming → không test được. | Open |
| Q17 | Low | UC203-208.1 mục 5: "Tham chiếu CMR_08" | CMR_08 hiện **"Chưa định nghĩa — Chờ BA xác nhận"**. Khi nào có quy tắc hiển thị kỳ hạn (tên kỳ, format, logic nhóm)? | Test case hiển thị header kỳ hạn bị chặn cho đến khi CMR_08 được định nghĩa. | Open |

---

## 🟢 What's Good

- **Feature Identity & Scope** rõ ràng: Mẫu II.4, phân hệ ODI, Admin site, định kỳ năm.
- **Phân quyền** chi tiết: ghi rõ CMR_03 (người tạo quản lý bản ghi), loại trừ CMR_01/CMR_02.
- **Validation đặc thù** cho Ngày ký và Năm báo cáo có message lỗi cụ thể.
- **Action Mapping** đầy đủ 7 hành động với điều kiện hiển thị và tham chiếu CF chính xác.
- **File đính kèm** có spec rõ: format, max size/file, icon xóa.

---

## 🧪 Testability Outlook

**CÓ THỂ test ngay:**
- Phân quyền: Admin site, người tạo xem/sửa bản ghi của mình.
- Validate: Ngày ký ≤ hôm nay, Năm báo cáo ≤ năm hiện tại, trường bắt buộc.
- Action state matrix: 7 button × 4 trạng thái (Lưu nháp/Chờ duyệt/Đã tiếp nhận/YC chỉnh sửa).
- File upload: format, size 10MB.

**CHƯA THỂ test (blocked):**
- UI layout, position, spacing (thiếu Mockup — Q1).
- Trạng thái sau Nộp: Chờ duyệt hay Đã tiếp nhận (Q2).
- Validate Số văn bản: free-text hay CMR_13 (Q4).
- Dirty Form Guard popup P02 (Q10).
- Luồng Import end-to-end (Q13).
- Nộp từ Danh sách fail behavior (Q14).
- Export file naming (Q16).

**Suggested test areas (sau khi giải quyết gaps):**
- Happy path: Lập → Lưu nháp → Chỉnh sửa → Nộp → verify trạng thái.
- Boundary: Max 3000 chars textarea, max 1000 chars Đề xuất, max 50 chars Số văn bản, file 10MB.
- Negative: Ngày ký tương lai, năm > hiện tại, upload file .png, file > 10MB.
- Integration: Export .docx verify naming, Import template flow, Audit Trail timeline.

---

## 8. Acceptance Criteria (AC)

**A. UI**
- **AC_UI_01:** Danh sách hiển thị dạng Periodic-single, nhóm theo Năm, mặc định collapse.
- **AC_UI_02:** Nút [Lập báo cáo] và [Import] chỉ hiển thị khi kỳ "Trong thời hạn". Ẩn hoàn toàn khi "Chưa tới hạn" hoặc "Qua kỳ".
- **AC_UI_03:** Màn hình Xem chi tiết: toàn bộ trường Disabled. Nút [Chỉnh sửa] ẩn khi trạng thái ≠ {Lưu nháp, YC chỉnh sửa}.

**B. Functional**
- **AC_FN_01:** Ngày ký > hôm nay → lỗi inline *"Ngày ký không được là ngày trong tương lai"*.
- **AC_FN_02:** Năm báo cáo không hợp lệ → lỗi inline *"Năm báo cáo không hợp lệ"*. Năm > hiện tại → *"Năm báo cáo không được vượt quá năm hiện tại"*.
- **AC_FN_03:** Nộp khi trường bắt buộc trống → inline đỏ *"Trường bắt buộc"* (V01).
- **AC_FN_04:** [Chờ Q2] Nộp thành công → trạng thái = [???], Toast T02 *"Đã nộp báo cáo thành công"*.
- **AC_FN_05:** Lưu nháp khi tất cả trường trống → Toast T07 *"Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"*.
- **AC_FN_06:** File upload sai định dạng → lỗi inline. File > 10MB → lỗi inline.
- **AC_FN_07:** Xóa chỉ khả dụng khi Lưu nháp VÀ chưa từng nộp → Popup P04 → Toast T08.

**C. Integration**
- **AC_INT_01:** Export → file .docx, tên file theo CF_04 [Chờ Q16].
- **AC_INT_02:** Xem vòng đời → popup timeline, sắp xếp thời gian tăng dần.
