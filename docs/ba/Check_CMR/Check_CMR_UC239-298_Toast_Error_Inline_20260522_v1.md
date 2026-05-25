# CHECK CMR & CF — TOAST / ERROR / INLINE MESSAGES CHO UC239-298

| Thuộc tính | Giá trị |
| --- | --- |
| **Tài liệu** | Danh sách Toast, Error, Inline Messages cần update cho UC239-298 |
| **Ngày tạo** | 2026-05-22 |
| **Tác giả** | QC Agent |
| **Phiên bản** | v1 |
| **Nguồn tham chiếu** | CMR_common_business_rules.md, CF_common_functions.md, list-toast-messages.md, Align_CMR_Report_20260520.md |

---

## 1. TOAST MESSAGES ÁP DỤNG CHO UC239-298

Các Toast message sau đây áp dụng chung cho **TẤT CẢ** UC239-298 (theo CF_01, CF_03, CF_04, CF_07, CF_08, CF_09):

| Mã | Trường hợp | Tiêu đề | Nội dung | Loại | Áp dụng CF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T01** | Lập báo cáo + Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | 🟢 Success | CF_01 |
| **T02** | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success | CF_01, CF_03, CF_09 |
| **T03** | Chỉnh sửa báo cáo + Lưu nháp thành công | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success | CF_03 |
| **T04** | Xuất báo cáo thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success | CF_04, CF_07 |
| **T05** | Lỗi hệ thống (API fail, lưu nháp fail, nộp fail, xuất fail) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error | CF_01–CF_09 |
| **T07** | Lưu nháp khi tất cả trường đều trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error | CF_01, CF_03 |
| **T08** | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success | CF_08 |

> **Lưu ý quan trọng:** Toàn bộ Toast/Error/Inline message **KHÔNG có dấu `.` ở cuối câu** (theo chuẩn Align_CMR_Report v7.0).

---

## 2. INLINE VALIDATION MESSAGES ÁP DỤNG CHO UC239-298

### 2.1. Inline chung — Trường bắt buộc (Required Fields)

| Loại trường | Message lỗi | Vị trí hiển thị | Tham chiếu CMR |
| :--- | :--- | :--- | :--- |
| Trường số (Numeric) bắt buộc bỏ trống | `"Vui lòng nhập [tên trường]"` | Bên dưới trường, màu đỏ | CMR_05 |
| Trường text bắt buộc bỏ trống | `"Vui lòng nhập [tên trường]"` | Bên dưới trường, màu đỏ | CMR_06 |
| Dropdown bắt buộc chưa chọn | `"Vui lòng chọn [tên trường]"` | Bên dưới trường, màu đỏ | CMR_07 |

**Hiển thị lỗi trong eForm Grid (lưới nhập liệu):**
- Lỗi hiển thị dạng **viền đỏ** quanh ô (không hiển thị text bên dưới do không gian hạn chế)
- Hover vào ô → hiển thị **tooltip** chứa message lỗi tương ứng

### 2.2. Inline — Trường số (Numeric Validation)

| Trường hợp | Message lỗi | Tham chiếu |
| :--- | :--- | :--- |
| Nhập ký tự không hợp lệ (chữ cái, ký tự đặc biệt ngoài `-`, `.`, `,`) | `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ"` | CMR_05, V02 |
| Trường yêu cầu ≥ 0: nhập dấu trừ `-` | `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"` | CMR_05, V03 |
| Nhập ký tự hợp lệ nhưng sai cấu trúc (nhiều dấu chấm, dấu phẩy sai vị trí) | `"Sai định dạng số"` | CMR_05, V04 |
| Vượt giới hạn digit precision (>15 nguyên hoặc >5 thập phân) | `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` | Align_CMR C05b |

### 2.3. Inline — Trường text (Text Validation)

| Trường hợp | Message lỗi | Tham chiếu |
| :--- | :--- | :--- |
| Vượt max length Textbox (255 ký tự) | `"[Tên trường] không được vượt quá 255 ký tự!"` | CMR_06, Align_CMR A06 |
| Vượt max length Textarea (3000 ký tự) | `"[Tên trường] không được vượt quá 3000 ký tự!"` | CMR_06, Align_CMR A06 |
| Chưa đủ min length | `"[Tên trường] nhập chưa đủ [minlength] ký tự!"` | CMR_06 |

### 2.4. Inline — Trường Mã (Code Field)

| Trường hợp | Message lỗi | Tham chiếu |
| :--- | :--- | :--- |
| Mã có khoảng trắng giữa hoặc tiếng Việt có dấu | `"Mã không bao gồm khoảng trắng và ký tự có dấu"` | Align_CMR B05 |
| Vượt max length (50 ký tự) | `"[Tên trường] không được vượt quá 50 ký tự!"` | Align_CMR B04 |

### 2.5. Inline — V16: Bảng động / Form rỗng khi Nộp

| Trường hợp | Message lỗi | UC áp dụng cụ thể |
| :--- | :--- | :--- |
| Bảng động rỗng (0 dòng) khi Nộp | `"Vui lòng khai báo ít nhất 1 [đối tượng] trong kỳ báo cáo"` | Tất cả UC245-298 |

**Mapping [đối tượng] theo từng UC:**

| UC | Đối tượng | Message cụ thể |
| :--- | :--- | :--- |
| UC239-244 | KCN | `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| UC245-250 | KCN | `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| UC251-256 | dự án hạ tầng KCN | `"Vui lòng khai báo ít nhất 1 dự án hạ tầng KCN trong kỳ báo cáo"` |
| UC257-262 | KCN | `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| UC263-268 | nhà máy XLNT | `"Vui lòng khai báo ít nhất 1 nhà máy XLNT trong kỳ báo cáo"` |
| UC269-274 | KCN | `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| UC275-280 | KCN | `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| UC281-286 | KKT | `"Vui lòng khai báo ít nhất 1 KKT trong kỳ báo cáo"` |
| UC287-292 | chỉ tiêu | `"Vui lòng khai báo ít nhất 1 chỉ tiêu trong kỳ báo cáo"` |
| UC293-298 | KKT | `"Vui lòng khai báo ít nhất 1 KKT trong kỳ báo cáo"` |

---

## 3. POPUP MESSAGES ÁP DỤNG CHO UC239-298

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P01** | Xác nhận trước khi nộp | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] (chỉ active khi checkbox tích) / [Hủy] / ✕ | CF_01, CF_03 |
| **P02** | Dirty Form Guard — dữ liệu chưa lưu | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] | CF_01, CF_03, CMR_14 |
| **P04** | Xác nhận trước khi xóa | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] | CF_08 |

---

## 4. ALERT MESSAGES (Popup Nhập từ file — CF_02)

| Mã | Trường hợp | Nội dung | Hành vi |
| :--- | :--- | :--- | :--- |
| **A01** | Dữ liệu không khớp Phạm vi | `"Dữ liệu không khớp với [Phạm vi báo cáo] đã chọn. Vui lòng kiểm tra lại"` | Giữ nguyên popup |
| **A02** | Cấu trúc file sai template | `"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải"` | Giữ nguyên popup |
| **A03** | File sai định dạng | `"Định dạng file không được hỗ trợ. Vui lòng sử dụng file template đã tải"` | Giữ nguyên popup |
| **A04** | File rỗng / không đọc được | `"Không thể đọc file. Vui lòng kiểm tra lại file và thử lại"` | Giữ nguyên popup |

---

## 5. VIOLATIONS CẦN SỬA TRONG UC239-298 (theo Align_CMR_Report)

### 5.1. Numeric digit precision — TẤT CẢ UC239-298

| UC | Hiện trạng | Cần sửa |
| :--- | :--- | :--- |
| UC239-244 | Không khai báo digit precision | Bổ sung: phần nguyên → **15 chữ số**, phần thập phân → block sau **5 chữ số** |
| UC245-250 | Không khai báo digit precision | Bổ sung tương tự |
| UC251-256 | Không khai báo digit precision | Bổ sung tương tự |
| UC257-262 | Không khai báo digit precision | Bổ sung tương tự |
| UC263-268 | Không khai báo digit precision | Bổ sung tương tự |
| UC269-274 | Không khai báo digit precision | Bổ sung tương tự |
| UC275-280 | Không khai báo digit precision | Bổ sung tương tự |
| UC281-286 | Không khai báo digit precision | Bổ sung tương tự |
| UC287-292 | Không khai báo digit precision | Bổ sung tương tự |
| UC293-298 | Không khai báo digit precision | Bổ sung tương tự |

**Error message khi vi phạm:** `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`

### 5.2. Textbox / Textarea max length — UC cụ thể

| UC | Trường | Hiện trạng | Cần sửa |
| :--- | :--- | :--- | :--- |
| UC245-250 | Fields 12, 13, 14 (textarea) | Max 1000 | Sửa → **3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự!"` |
| UC263-268 | Thời gian dự kiến hoàn thành (textbox) | Max 50 | Sửa → **255 ký tự**. Error: `"Thời gian dự kiến hoàn thành không được vượt quá 255 ký tự!"` |
| UC263-268 | Quy mô công nghệ (textbox) | Chưa khai báo max | Khai báo → **255 ký tự**. Error: `"Quy mô công nghệ không được vượt quá 255 ký tự!"` |
| UC263-268 | Tất cả textarea fields | Max 1000 | Sửa → **3000 ký tự**. Error: `"[Tên trường] không được vượt quá 3000 ký tự!"` |

### 5.3. Code field — UC239-298

| UC | Trường | Hiện trạng | Cần sửa |
| :--- | :--- | :--- | :--- |
| UC239-298 | Mã KCN / Mã dự án | Max length không đồng nhất | Chuẩn hóa max = **50 ký tự**. Error: `"Mã không bao gồm khoảng trắng và ký tự có dấu"` |

### 5.4. CMR_16 — Filter Dropdown thiếu option "Tất cả"

| UC | Vị trí | Hiện trạng | Cần sửa |
| :--- | :--- | :--- | :--- |
| UC293-298 | Filter Multi-select Dropdown (dòng 2-3 bảng field UC293-298.1) | Thiếu tham chiếu CMR_16 | Bổ sung tham chiếu CMR_16: Filter dropdown phải có option "Tất cả" mặc định |

### 5.5. Placeholder chuẩn

| Loại trường | Placeholder chuẩn | Tham chiếu |
| :--- | :--- | :--- |
| Textbox / Numeric | `"Nhập [tên trường]"` | CMR_05, CMR_06 |
| Dropdown (form) | `"Chọn [tên trường]"` | CMR_07 |
| Search box | `"Tìm kiếm nhanh theo [điều kiện]"` | CMR_06 |
| Filter dropdown | Mặc định chọn `"Tất cả"` | CMR_16 |

> **UC239-298 Search placeholder:** `"Tìm kiếm nhanh theo mã báo cáo"` — ✅ Đã đúng chuẩn, không cần sửa.

---

## 6. TỔNG HỢP THEO TỪNG UC — ACTIONS CẦN THỰC HIỆN

### UC239-244 (Biểu 2101 — Thu hút đầu tư KCN)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 cho tất cả trường số |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| 3 | Toast T01/T02/T03/T05/T07/T08 | Verify đã tham chiếu đầy đủ |
| 4 | Popup P01/P02/P04 | Verify đã tham chiếu đầy đủ |
| 5 | Required fields | Verify message: `"Vui lòng nhập [tên trường]"` / `"Vui lòng chọn [tên trường]"` |
| 6 | CMR_14 Dirty Form Guard | Verify áp dụng đúng (in-memory khi chuyển tab FDI/DDI) |

### UC245-250 (Biểu 2102 — Thành lập, điều chỉnh KCN)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | Textarea max | Sửa Fields 12, 13, 14 từ max 1000 → **3000** |
| 3 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| 4 | Toast T01/T02/T03/T05/T07/T08 | Verify đã tham chiếu đầy đủ |
| 5 | Required fields | Verify message chuẩn, bỏ dấu `.` nếu có (Row 83 có `.`) |

### UC251-256 (Biểu 2103 — Dự án hạ tầng KCN)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 dự án hạ tầng KCN trong kỳ báo cáo"` |
| 3 | Toast/Popup | Verify đầy đủ |
| 4 | Required fields | Verify message chuẩn |

### UC257-262 (Biểu 2104 — SXKD tại KCN)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| 3 | Toast/Popup | Verify đầy đủ |
| 4 | Required fields | Verify message chuẩn |

### UC263-268 (Biểu 2105 — Nhà máy XLNT KCN)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | Textbox max | Sửa "Thời gian dự kiến hoàn thành" max 50 → **255** |
| 3 | Textbox max | Khai báo "Quy mô công nghệ" max → **255** |
| 4 | Textarea max | Sửa tất cả textarea từ max 1000 → **3000** |
| 5 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 nhà máy XLNT trong kỳ báo cáo"` |
| 6 | Toast/Popup | Verify đầy đủ |
| 7 | Required fields | Verify message chuẩn |

### UC269-274 (Biểu 2106 — Lao động KCN)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| 3 | Toast/Popup | Verify đầy đủ |
| 4 | Required fields | Verify message chuẩn |

### UC275-280 (Biểu 2107 — Danh mục KCN quy hoạch)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |
| 3 | Toast/Popup | Verify đầy đủ |
| 4 | Required fields | Verify message chuẩn |

### UC281-286 (Biểu 2108 — Số lượng DT KKT)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KKT trong kỳ báo cáo"` |
| 3 | Toast/Popup | Verify đầy đủ |
| 4 | Required fields | Verify message chuẩn |

### UC287-292 (Biểu 2109 — Thu hút đầu tư KKT) ⚠️ TRỌNG TÂM

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Form rỗng khi Nộp | Thêm inline/toast: `"Vui lòng khai báo ít nhất 1 chỉ tiêu trong kỳ báo cáo"` |
| 3 | **THIẾU 4 FIELDS** | Bổ sung "Số DN đang hoạt động" + "Số lao động" cho FDI và DDI (Phần A) |
| 4 | Toast/Popup | Verify đầy đủ |
| 5 | Required fields | Verify message chuẩn — `"Vui lòng nhập [tên trường]"` |
| 6 | Field 11 cho phép âm | Áp dụng V02 (cho phép dấu `-`), KHÔNG áp dụng V03 |

### UC293-298 (Biểu 2110 — Quy hoạch đất KKT)

| # | Hạng mục | Action |
| :--- | :--- | :--- |
| 1 | Numeric digit precision | Bổ sung rule 15+5 |
| 2 | V16 — Bảng rỗng khi Nộp | Thêm inline: `"Vui lòng khai báo ít nhất 1 KKT trong kỳ báo cáo"` |
| 3 | **CMR_16** | Bổ sung tham chiếu CMR_16 cho filter dropdown — option "Tất cả" mặc định |
| 4 | Toast/Popup | Verify đầy đủ |
| 5 | Required fields | Verify message chuẩn |

---

## 7. QUY TẮC CHUNG VỀ FORMAT ERROR MESSAGE

| # | Quy tắc | Ví dụ |
| :--- | :--- | :--- |
| 1 | **KHÔNG có dấu `.` ở cuối** tất cả error/toast/inline message | ✅ `"Vui lòng nhập Số dự án"` ❌ `"Vui lòng nhập Số dự án."` |
| 2 | Required Numeric/Text dùng `"Vui lòng nhập [tên trường]"` | `"Vui lòng nhập Tổng vốn đầu tư đăng ký"` |
| 3 | Required Dropdown dùng `"Vui lòng chọn [tên trường]"` | `"Vui lòng chọn Năm báo cáo"` |
| 4 | Toast T05 bỏ `.` cuối | `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"` |
| 5 | Empty state không có `.` | `"Không có dữ liệu"` (không phải `"Không có dữ liệu."`) |
| 6 | Không tìm thấy kết quả search | `"Không tìm thấy kết quả phù hợp"` |

---

## 8. THAM CHIẾU CMR/CF BẮT BUỘC CHO UC239-298

Mỗi UC trong nhóm UC239-298 **BẮT BUỘC** phải tham chiếu các rule sau:

| Rule | Mô tả | Áp dụng |
| :--- | :--- | :--- |
| CMR_04 | Trạng thái kỳ hạn báo cáo | Điều kiện hiển thị nút Lập/Nhập từ file |
| CMR_05 | Quy tắc trường số | Tất cả trường numeric |
| CMR_06 | Quy tắc trường text | Tất cả trường text/textarea |
| CMR_07 | Quy tắc dropdown | Tất cả dropdown |
| CMR_12 | Trạng thái trường API | Trường auto-fill từ API |
| CMR_14 | Dirty Form Guard | Popup cảnh báo khi rời form |
| CMR_15 | Thêm/Xóa hàng bảng động | Bảng nhập liệu có thêm/xóa hàng |
| CMR_16 | Filter Dropdown "Tất cả" | Filter trên màn hình danh sách |
| CMR_18 | Tab Navigation | Form nhập liệu |
| CF_01 | Lập báo cáo | Luồng tạo mới |
| CF_02 | Nhập từ file | Luồng import |
| CF_03 | Chỉnh sửa | Luồng edit |
| CF_04 | Xuất báo cáo | Luồng export |
| CF_06 | Xem vòng đời | Audit trail |
| CF_07 | Xem chi tiết | View detail |
| CF_08 | Xóa báo cáo | Luồng delete |
| CF_09 | Nộp từ Danh sách | Submit from listing |

---

*Kết thúc tài liệu.*

