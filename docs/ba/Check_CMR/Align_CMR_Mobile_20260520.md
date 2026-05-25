# ALIGN CMR MOBILE — 20260520

**Tiêu đề:** Align CMR Mobile — Rà soát & cập nhật toàn diện
**Ngày tạo:** 2026-05-20
**Tác giả:** Antigravity Agent
**Phiên bản:** v6.1
**Ghi chú:** Kế thừa toàn bộ v5.1. Bổ sung impact analysis chi tiết cho các UC còn thiếu sau khi đọc trực tiếp từng file SRS-mobile.

---

## A. TRƯỜNG TEXT (Textbox / Textarea) — CMR-09

| ID | Tiêu chí | Rule đã xác nhận | Trạng thái | Ghi chú thay đổi |
|:---|:---|:---|:---:|:---|
| A01 | Tự động xóa khoảng trắng đầu/cuối | Hệ thống tự động xóa khoảng trắng ở đầu và cuối giá trị người dùng nhập **khi out-click**. VD: `" Nguyễn Văn A "` → `"Nguyễn Văn A"` | ✅ Xác nhận | ⚠️ CHANGED: timing là **out-click** (không phải trước validate/submit) |
| A02 | Người dùng chỉ nhập toàn khoảng trắng | Sau khi xóa khoảng trắng thừa, nếu không còn ký tự nào → coi như chưa nhập gì → trường bắt buộc hiển thị lỗi `"Vui lòng nhập [tên trường]"" | ✅ Xác nhận | |
| A03 | Áp dụng cho ô nhập mật khẩu (Password) | Có — mật khẩu cũng bị xóa khoảng trắng đầu/cuối | ✅ Xác nhận | |
| A04 | Thông báo lỗi khi bỏ trống bắt buộc | `"Vui lòng nhập [tên trường]"" — VD: `"Vui lòng nhập Họ và tên"" | ✅ Xác nhận | |
| A05 | Placeholder text box / text area | `"Nhập [tên trường]"" | ✅ Xác nhận | |
| A06 | Độ dài tối đa mặc định | - **Textbox: 255 ký tự**<br>- **Textarea: 3000 ký tự**<br>- Các trường có rule riêng sẽ được quy định rõ trong SRS từng UC | ✅ **BA CONFIRMED: 255** | ⚠️ CHANGED: Textbox 255 (không phải 500), Textarea 3000 |
| A07 | Thông báo lỗi khi nhập quá số ký tự | `"[Tên trường] không được vượt quá [maxlength] ký tự!"` | ✅ Xác nhận | ⚠️ CHANGED: format mới có `[maxlength]` và dấu `!` |
| A08 | Thông báo lỗi khi nhập chưa đủ ký tự tối thiểu | `"[Tên trường] nhập chưa đủ [minlength] ký tự!"` | ✅ Xác nhận | ⚠️ CHANGED: thêm `[minlength]` cụ thể và dấu `!` |

### Phân tích ảnh hưởng — Mục A

| UC | Trường bị ảnh hưởng | Loại trường | Hiện trạng trong SRS | Thay đổi cần thực hiện |
|:---|:---|:---|:---|:---|
| **UC252** | Họ và tên | Textbox | Max 50 ký tự. Error required thiếu `!`. | Sửa error required → `"Vui lòng nhập Họ và tên"`. Sửa error vượt max → `"Họ và tên không được vượt quá 50 ký tự!"`. |
| **UC252** | Nơi cấp | Textbox | Max 500 ký tự. Error sai format. | Sửa max → **255 ký tự**. Sửa error → `"Nơi cấp không được vượt quá 255 ký tự!"`. |
| **UC252** | Email | Textbox | Max 100 ký tự. Error thiếu `!`. | Sửa error → `"Email không được vượt quá 100 ký tự!"`. |
| **UC252** | Mật khẩu, Xác nhận MK | Password | Error required thiếu `!`. | Sửa error required → `"Vui lòng nhập [tên trường]"". |
| **UC249** | Email | Textbox | Max 100 ký tự. Error sai format, thiếu `!`. | Sửa error → `"Email không được vượt quá 100 ký tự!"`. |
| **UC249** | Địa chỉ | Textbox | Max 500 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). Sửa error → `"Địa chỉ không được vượt quá 255 ký tự!"`. |
| **UC249** | Mã bưu chính | Textbox | Bỏ toàn bộ validation. Cho phép nhập tự do. | ✅ **EXCEPTION**: Mã bưu chính nhập freetext, không giới hạn độ dài. Không sửa gì thêm. |
| **UC250** | Chức vụ / Chức danh | Textbox | Max 50 ký tự. Error sai format, thiếu `!`. | Sửa error → `"Chức vụ / Chức danh không được vượt quá 50 ký tự!"`. |
| **UC250** | Nơi cấp người đại diện | Textbox | Max 500 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). Sửa error → `"Nơi cấp không được vượt quá 255 ký tự!"`. |
| **UC250** | Tên tổ chức, Tên viết tắt | Textbox | Max length chưa khai báo rõ. Error required thiếu `!`. | Khai báo max = **255 ký tự**. |
| **UC53** | Họ và tên (Cá nhân) | Textbox | Max 200 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). |
| **UC53** | Địa chỉ (Cá nhân & Tổ chức/DN) | Textbox | Max 500 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). |
| **UC53** | Người đại diện, Chức vụ | Textbox | Max 500 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). |
| **UC53** | Tiêu đề phản ánh | Textbox | Max 200 ký tự. Placeholder sai chuẩn. Error required thiếu `!`. | Sửa placeholder `"Nhập Tiêu đề phản ánh"`. |
| **UC53** | Nội dung phản ánh | Textarea | Max 10.000 ký tự (sai rule chung G02). Placeholder có `...`. | Sửa → **3000 ký tự** (rule chung Textarea). Bỏ `...` khỏi placeholder. |
| **UC251, UC253, UC256** | Mật khẩu hiện tại/mới | Password | Error required thiếu `!`. | Sửa error required → `"Vui lòng nhập [tên trường]"". |
| **UC87 (v1.6)** | Quy mô vốn dự kiến | Textbox (Numeric) | Max **500 ký tự** (sai rule chung G04=255). Error vượt max hiện tại: `"Quy mô vốn dự kiến nhập quá ký tự cho phép"` — đúng format H05, chỉ sai max length. | Sửa max length → **255 ký tự**. Error message giữ nguyên format H05. |

---

## B. TRƯỜNG MÃ (Code Field) — CMR mới

| ID | Tiêu chí | Rule đã xác nhận | Trạng thái | Ghi chú thay đổi |
|:---|:---|:---|:---:|:---|
| B01 | Tự động xóa khoảng trắng đầu/cuối | Hệ thống tự động xóa khoảng trắng ở đầu và cuối **khi out-click**. VD: `" ABC123 "" → `"ABC123"" | ✅ Xác nhận | |
| B02 | Người dùng chỉ nhập toàn khoảng trắng | Sau khi xóa, nếu rỗng → coi như chưa nhập → lỗi `"Vui lòng nhập [tên trường]"" | ✅ Xác nhận | |
| B03 | Placeholder | `"Nhập [tên trường]"" | ✅ Xác nhận | |
| B04 | Độ dài tối đa mặc định | **50 ký tự** | ✅ Xác nhận | ⚠️ CHANGED: 50 (không phải 500) |
| B05 | Thông báo lỗi khi nhập khoảng trắng ở giữa và tiếng Việt có dấu | `"Mã không bao gồm khoảng trắng và ký tự có dấu"` | ✅ Xác nhận | ⚠️ NEW RULE |

### Phân tích ảnh hưởng — Mục B

| UC | Trường bị ảnh hưởng | Loại trường | Hiện trạng trong SRS | Thay đổi cần thực hiện |
|:---|:---|:---|:---|:---|
| **UC252** | Mã định danh (CCCD) | Textbox (numeric) | Max 12 số. Error: `"Mã định danh chỉ gồm các số 0-9."` (có dấu `.`). | Cập nhật bắt buộc đúng **12 số**. Áp dụng rule B05. Sửa error. |
| **UC252** | Mã số thuế | Textbox (numeric) | Max 10/13 số. Error sai format, thiếu `!`. | Cập nhật độ dài (Cá nhân đúng **12 số**, DN đúng **10 số**). Áp dụng rule B05. |
| **UC252** | Mã định danh (Tổ chức) | Textbox (numeric) | Error: `"Mã định danh chỉ gồm các số 0-9."` | Cập nhật bắt buộc đúng **12 số**. Áp dụng rule B05. |
| **UC249** | Mã bưu chính | Textbox | Bỏ toàn bộ validation. | ✅ **EXCEPTION**: Nhập freetext, không áp dụng rule B05. |
| **UC250** | Mã định danh người ĐD | Textbox (numeric) | Error: `"Mã định danh nhập quá ký tự cho phép"`. | Cập nhật bắt buộc đúng **12 số**. Áp dụng rule B05. |
| **UC253** | Mã định danh | Textbox (numeric) | Error: `"Mã định danh chỉ gồm các số 0-9."` | Cập nhật độ dài (Cá nhân **12 số**, DN **10 số**). Áp dụng rule B05. |
| **UC256** | Mã định danh | Textbox (numeric) | Error thiếu `!`, có dấu `.`. | Cập nhật độ dài (Cá nhân **12 số**, DN **10 số**). Áp dụng rule B05. Sửa format. |

---

## C. TRƯỜNG SỐ (Numeric) — CMR-11

| ID | Tiêu chí | Rule đã xác nhận | Trạng thái | Ghi chú thay đổi |
|:---|:---|:---|:---:|:---|
| C01 | Placeholder | C02 | Ký tự hợp lệ | C03 | Trường >= 0 | C04 | Không cắt thập phân | C05 | Max length mặc định | **255 ký tự** (max length này sẽ thay đổi tùy theo 1 số trường có rule riêng) | ✅ Xác nhận | ⚠️ CHANGED: 255 (không phải 500) |
| C06 | Error — Bắt buộc | `"Vui lòng nhập [tên trường]"` | ✅ Xác nhận | |
| C07 | Error — Vượt max length ### Phân tích ảnh hưởng — Mục C

| UC | Trường bị ảnh hưởng | Hiện trạng | Thay đổi cần thực hiện |
|:---|:---|:---|:---|
| **UC249, UC250, UC252, UC53** | Số điện thoại | Error message cũ có `.`. Error required thiếu `!`. | Sửa error required → `"Vui lòng nhập Số điện thoại!"`. |
| **UC249** | Số điện thoại | Error chưa đủ số: `"Số điện thoại nhập chưa đủ ký tự cho phép"` (sai format H04). | Sửa → `"Số điện thoại nhập chưa đủ [N] ký tự!"`. |
| **UC53** | **UC2** | Diện tích từ / đến | Max 500 ký tự (là Numeric). | Sửa max length → 255 ký tự. |

| UC | Trường bị ảnh hưởng | Hiện trạng | Thay đổi cần thực hiện |
|:---|:---|:---|:---|
| **UC249** | Số điện thoại | Error required: `"Vui lòng nhập Số điện thoại"` (thiếu `!`). Error chưa đủ số: `"Số điện thoại nhập chưa đủ ký tự cho phép"` (sai format H04). Error vượt: `"Số điện thoại nhập quá ký tự cho phép"` (sai format H05). | Sửa error chưa đủ → `"Số điện thoại nhập chưa đủ [N] ký tự!"`. |
| **UC53** ---

## D. DROPDOWN / COMBOBOX — CMR-03

| ID | Tiêu chí | Rule đã xác nhận | Trạng thái | Ghi chú thay đổi |
|:---|:---|:---|:---:|:---|
| D01 | Placeholder mặc định trong form | D02 | Giá trị mặc định trong filter dropdown | D03 | Error — Bắt buộc chưa chọn | `"Vui lòng chọn [tên trường]"` | ✅ Xác nhận | |
| D04 | Không tìm thấy kết quả | D05 | Highlight option đã chọn khi mở lại | D06 | Tên quá dài | D07 | Searchable Dropdown — Hiển thị Placeholder khi clear | Khi xóa hết keyword → dropdown hiển thị lại **placeholder** | ✅ Xác nhận | ⚠️ NEW RULE |
| D08 | Searchable Dropdown — Tap ra ngoài khi đang clear | Nếu clear (trống) mà tap ra ngoài → chọn lại **"Tất cả"** (với filter) hoặc rỗng (với form bắt buộc) | ✅ Xác nhận | ⚠️ NEW RULE |

### Phân tích ảnh hưởng — Mục D

| UC | Trường bị ảnh hưởng | Loại trường | Hiện trạng | Thay đổi cần thực hiện |
|:---|:---|:---|:---|:---|
| **UC249, 250, 53** | Quốc gia, Tỉnh/TP, Phường/Xã | **UC250, 252** | Ngày sinh, Ngày cấp | **UC53** | Chủ đề phản ánh, Đơn vị tiếp nhận | **UC53** | Tỉnh/Thành phố, Xã/Phường | **UC45-51** | Dropdown filter | **UC2** | Tỉnh/Thành (filter) | Searchable Dropdown | Thiếu rule mô tả clear keyword. | Bổ sung D07 + D08 (Tap ra ngoài → "Tất cả tỉnh thành"). |
| **UC7-11, 12-16, 17-21, 22-26, 27-31, 40, 41, 58, 70, 87** | Các filter: KKT, KCN, NĐT, Lĩnh vực... | Searchable Dropdown | Thiếu rule mô tả clear keyword. | Bổ sung D07 + D08 tương ứng. |
| **UC42-44, 53, 45-51** | Dropdown trong Bottom Sheet | Dropdown Filter | Thiếu hành vi xóa keyword. | Bổ sung D07 + D08 cho hành vi xóa keyword. |

| UC | Trường bị ảnh hưởng | Loại | Hiện trạng | Thay đổi cần thực hiện |
|:---|:---|:---|:---|:---|
| **UC53** | Chủ đề phản ánh, Đơn vị tiếp nhận | **UC53** | Tỉnh/Thành phố, Xã/Phường (Cá nhân & Tổ chức) | **UC249** | Quốc gia, Tỉnh/Thành phố, Phường/Xã | **UC45-51** | Dropdown Trạng thái (filter) | Dropdown | Empty text trong danh sách option: `"Không có dữ liệu."` có dấu `.`. | → `"Không có dữ liệu"`. |

---

## E. Ô TÌM KIẾM (Search Box) — CMR-01

| ID | Tiêu chí | Rule đã xác nhận | Trạng thái | Ghi chú thay đổi |
|:---|:---|:---|:---:|:---|
| E01 | Placeholder | E02 | Tìm kiếm tự động (không cần Enter) | E03 | Loại tìm kiếm | E04 | Tự động xóa khoảng trắng đầu/cuối từ khóa | E05 | Max length | **255 ký tự** | ✅ Xác nhận | ⚠️ CHANGED: 255 (không phải 500) |
| E06 | Xóa hết từ khóa ### Phân tích ảnh hưởng — Mục E

| UC | Trường bị ảnh hưởng | Hiện trạng trong SRS | Thay đổi cần thực hiện |
|:---|:---|:---|:---|
| **UC2, 7-11, 12-16, 17-21, 22-26, 27-31, 40, 41, 52, 58, 70, 90** | Tất cả ô Tìm kiếm chính | Max length = **500 ký tự**. | Đổi max length → **255 ký tự**. |
| **UC42-44** | Ô tìm kiếm lịch hẹn | Max **500 ký tự** (ghi rõ trong SRS). Placeholder: `"Tìm kiếm nhanh theo tên thủ tục"`. | Đổi max → **255 ký tự**. Placeholder đúng chuẩn — giữ nguyên. |
| **UC12-16, 56-57, 60-61** | Ô tìm kiếm / Chatbot | Placeholder có chứa dấu `...`. | Bỏ dấu `...` theo chuẩn CMR. |
| **UC45-51** | Ô tìm kiếm hồ sơ | Max length chưa khai báo rõ trong SRS. | Khai báo max length **255 ký tự**. |
| **UC53** | Ô tìm kiếm phản ánh | Max chưa khai báo. Placeholder đúng chuẩn. | Khai báo max length **255 ký tự**. |
| **UC87** | Ô tìm kiếm | Max chưa khai báo rõ. | Khai báo max 255. ✅ **EXCEPTION**: Giữ nguyên placeholder "Tìm kiếm nhanh theo tên dự án". |
| **UC76-82** | Ô tìm kiếm FAQ | Max **500 ký tự** (ghi rõ trong SRS §2.1 row 5). Placeholder: `"Tìm kiếm nhanh theo câu hỏi, từ khoá"`. | Đổi max length → **255 ký tự**. Placeholder đúng chuẩn — giữ nguyên. |

| UC | Trường bị ảnh hưởng | Hiện trạng trong SRS | Thay đổi cần thực hiện |
|:---|:---|:---|:---|
| **UC42-44** | Ô tìm kiếm lịch hẹn | Max length **500 ký tự** (ghi rõ trong SRS). Placeholder: `"Tìm kiếm nhanh theo tên thủ tục"`. | Đổi max length → **255 ký tự**. Placeholder đúng chuẩn — giữ nguyên. |
| **UC45-51** | Ô tìm kiếm hồ sơ | Max length chưa khai báo rõ trong SRS. | Khai báo max length **255 ký tự**. |
| **UC53** | Ô tìm kiếm phản ánh | Placeholder: `"Tìm kiếm nhanh theo mã phản ánh"` — đúng chuẩn. Max chưa khai báo. | Khai báo max length **255 ký tự**. |

---

## F. LABEL — F01

| ID | Tiêu chí | Rule đã xác nhận | Trạng thái | Ghi chú |
|:---|:---|:---|:---:|:---|
| F01 | Trường bắt buộc | Đánh dấu `*` cạnh label | ✅ Xác nhận | |

### Phân tích ảnh hưởng — Mục F

| UC Bị Ảnh Hưởng | Hiện Trạng | Hành Động Cập Nhật Cần Thiết |
|:---|:---|:---|
| **Tất cả form** | Đã hiển thị dấu `*` nhưng cần đảm bảo nhất quán. | Map chuẩn trong UI Wireframe. |

---

## G. TỔNG HỢP MAX LENGTH

| ID | Loại trường | Max Length | Trạng thái |
|:---|:---|:---:|:---:|
| G01 | Textbox | **255 ký tự** | ✅ Xác nhận |
| G02 | Textarea | **3000 ký tự** | ✅ Xác nhận |
| G03 | Trường Mã (Code) | **50 ký tự** | ✅ Xác nhận |
| G04 | Trường Số (Numeric) | **255 ký tự** | ✅ Xác nhận |
| G05 | Search Box | **255 ký tự** | ✅ Xác nhận |
| G06 | Password | **50 ký tự** (rule riêng — đã xác nhận trong UC251, UC252, UC256) | ✅ Rule riêng |

### Phân tích ảnh hưởng — Mục G

| UC Bị Ảnh Hưởng | Hiện Trạng | Hành Động Cập Nhật |
|:---|:---|:---|
| **UC53** (Upload file) | Rule riêng: PDF, DOC, DOCX, JPG, PNG; tối đa 10MB/file. Không có common CMR rule. | ✅ Giữ rule riêng trong SRS UC53. Không đưa vào CMR common. |
| **UC53** (Họ và tên Cá nhân) | Max 200 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). |
| **UC53** (Địa chỉ, Người đại diện, Chức vụ) | Max 500 ký tự (sai rule chung G01). | Sửa → **255 ký tự** (rule chung Textbox). |
| **UC53** (Nội dung phản ánh — Textarea) | Max 10.000 ký tự (sai rule chung G02). | Sửa → **3000 ký tự** (rule chung Textarea). |
| **UC42-44** (Search box) | Max 500 ký tự (sai rule chung G05). | Sửa → **255 ký tự** (rule chung Search Box). |

---

## H. TỔNG HỢP ERROR MESSAGE

| ID | Loại lỗi | Message chuẩn | Trạng thái |
|:---|:---|:---|:---:|
| H01 | Bắt buộc — Text / Numeric / Password | `"Vui lòng nhập [tên trường]"` | ✅ Xác nhận |
| H02 | Bắt buộc — Dropdown | `"Vui lòng chọn [tên trường]"` | ✅ Xác nhận |
| H03 | Vượt max length (Text) | `"[Tên trường] không được vượt quá [maxlength] ký tự!"` | ✅ Xác nhận |
| H04 | Chưa đủ min length (Text) | `"[Tên trường] nhập chưa đủ [minlength] ký tự!"` | ✅ Xác nhận |
| H05 | Vượt max length (Numeric) | `"[Tên trường] nhập quá ký tự cho phép"` | ✅ Xác nhận |
| H06 | Trường Mã — Khoảng trắng giữa / tiếng Việt có dấu | `"Mã không bao gồm khoảng trắng và ký tự có dấu"` | ✅ Xác nhận |

### Phân tích ảnh hưởng — Mục H


| UC Bị ảnh Hưởng | Hiện Trạng | Hành Động Cần Thực Hiện |
|:---|:---|:---|
| **Tất cả các UC** | Các inline validation error có dấu `.` cuối câu. | Bỏ dấu `.` khỏi inline validation errors. |
| **UC254-258-259-260** | Toast/Popup/Error message có dấu `.` cuối câu: "nữa.", "15 phút.", "thử lại.", "thử lại sau.", "bị xóa." | Bỏ dấu `.` cuối tất cả toast, popup, error message. ✅ **Đã sửa v2.17** |

---

## I. BUTTON — CMR-01 (Luôn Enabled)

| ID | Button | Điều kiện Disabled | Điều kiện Enabled | Trạng thái | Ghi chú |
|:---|:---|:---|:---|:---:|:---|
| I01 | Submit / Lưu / Gửi | — (Không disable kể cả khi form chưa hợp lệ) | Luôn enabled | ✅ Xác nhận | Validate khi người dùng tap |
| I02 | Submit — Khi gọi API | Đang load API | Sau khi API trả về | ✅ Xác nhận | Tránh double-click |
| I03 | Submit — Double-tap | Xử lý bằng loading state / debounce | — | ✅ Xác nhận | |
| I04 | Nút Xác nhận (Dialog) | — | Luôn enabled | ✅ Xác nhận | |
| I05 | Nút Hủy (Dialog) | — | Luôn enabled | ✅ Xác nhận | |
| I06 | Nút Áp dụng (Filter) | — | Luôn enabled | ✅ Xác nhận | Kể cả khi validate filter sai |
| I07 | Nút Đặt lại (Filter) | — | Luôn enabled | ✅ Xác nhận | |
| I08 | Nút Thử lại (Error) | Khi đang load API | Sau timeout / lỗi | ✅ Xác nhận | |

### Phân tích ảnh hưởng — Mục I

| UC | Button bị ảnh hưởng | Hiện trạng trong SRS | Thay đổi cần thực hiện |
|:---|:---|:---|:---|
| **UC7-11, 12-16, 17-21, 22-26, 27-31, 40** | Nút "Áp dụng" (Filter) | **Disabled** khi có validation error. | Sửa → **Luôn Enabled**. Tap → validate → hiện lỗi inline. |
| **UC87 (v1.6)** | Nút "Xem dự án phù hợp" | **Disabled** khi chưa điền đủ trường bắt buộc. | Sửa → **Luôn Enabled**. Tap → validate. |
| **UC252** | Nút "Đăng ký" | **Disabled** khi form lỗi hoặc chưa check Điều khoản. | Sửa → **Luôn Enabled**. Tap → validate toàn bộ. |
| **UC256** | Nút "Đăng nhập" | **Disabled** khi có trường rỗng hoặc lỗi. | Sửa → **Luôn Enabled**. |
| **UC251** | Nút "Cập nhật mật khẩu" | **Disabled** khi form chưa hợp lệ (AC-07 tường minh). | Sửa → **Luôn Enabled**. Tap → validate → hiển thị lỗi inline. Cập nhận AC-07. |
| **UC253** | Nút "Gửi email", "Đặt lại MK" | **Disabled** khi form chưa hợp lệ. | Sửa → **Luôn Enabled**. |
| **UC53** | Nút "Gửi phản ánh" | **Disabled** mặc định khi form chưa hợp lệ. | Sửa → **Luôn Enabled**. Tap → validate. |
| **UC249, 250** | Nút "Lưu thay đổi" | **Disabled** khi chưa thay đổi so với data gốc. | Sửa → **Luôn Enabled** (I01). |
| **Tất cả UC có API** | Nút Call API | Chưa mô tả loading state rõ ràng. | Bổ sung: Tap → **loading state (spinner)** → sau khi API trả về mới enable lại. |


---

## K. MA TRẬN UC VÀ CÁC MỤC CMR BỊ ẢNH HƯỞNG (v6 — Full Scan)

| UC | A (Text) | B (Code) | C (Numeric) | D (Dropdown) | E (Search) | H (Error `.`) | I (Button) | Ghi chú |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **UC1** | — | — | — | — | — | — | — | Giữ nguyên |
| **UC2** | — | — | C05 | D07/D08 | E05 | ✅ | — | Search max 500→255 |
| **UC7-11** | — | — | — | D07/D08 | E05 | ✅ | I06 | Filter Áp dụng |
| **UC12-16** | — | — | — | D07/D08 | E05 | ✅ | I06 | Search placeholder có `...` |
| **UC17-21** | — | — | — | D07/D08 | E05 | ✅ | I06 | |
| **UC22-26** | — | — | — | D07/D08 | E05 | ✅ | I06 | |
| **UC27-31** | — | — | — | D07/D08 | E05 | ✅ | I06 | |
| **UC40** | — | — | — | D07/D08 | E05 | ✅ | I06 | |
| **UC41** | — | — | — | — | E05 | ✅ | — | |
| **UC42-44** | — | — | — | D07/D08 | E05 | ✅ | — | Search max 500→255 |
| **UC45-51** | — | — | — | D (empty) | E05 | ✅ | — | Date valid thiếu `!` |
| **UC52** | — | — | — | — | E05 | ✅ | — | |
| **UC53** | ✅ | — | C06 | D03 | E05 | ✅ | I01 | Nhiều vấn đề — xem mục A,H,I |
| **UC58** | — | — | — | D07/D08 | E05 | — | — | Không có inline validation error (chỉ system error/empty state → giữ nguyên) |
| **UC59** | — | — | — | D07/D08 | E05 | ✅ | I06 | Bổ sung align v2.3: max search 255, D07/D08, I06, bỏ `.` empty state |
| **UC62** | — | — | — | D07/D08 | E05 | — | — | Bổ sung v6.1: max search 255, D07/D08 cho Searchable Dropdown |
| **UC69** | — | — | — | D07/D08 | E05 | — | — | Bổ sung v6.1: max search 255, Textbox 255, D07/D08, I02 nút Tải về |
| **UC70** | — | — | — | D07/D08 | E05 | ✅ | I06 | Align v5.4: D07/D08, I06, bỏ `.` error |
| **UC76-82** | — | — | — | — | E05 | ✅ | — | Search max 500→255 |
| **UC83-86** | — | — | — | — | — | ✅ | — | Empty state thiếu `.` (CMR-14) |
| **UC87** | A07 | — | — | D07/D08 | E05 | ✅ | I01 | Nút Xem DK Enabled |
| **UC90** | — | — | — | — | E05 | ✅ | — | |
| **UC229-243** | — | — | — | — | — | — | — | Giữ nguyên |
| **UC249** | ✅ | — | ✅ | D03 | — | ✅ | I01 | Địa chỉ 255 (rule chung), error format |
| **UC250** | ✅ | B05 | — | D03 | — | ✅ | I01 | Địa chỉ 255 (rule chung) |
| **UC251** | ✅ | — | — | — | — | ✅ | I01 | Nút Disabled → Enabled |
| **UC252** | ✅ | ✅ | — | D03 | — | ✅ | I01 | (Đã phân tích v5) |
| **UC253** | ✅ | ✅ | — | — | — | ✅ | I01 | (Đã phân tích v5) |
| **UC254-260** | — | — | — | — | — | ✅ | — | Toast/Popup/Error bỏ dấu `.` — **Đã sửa v2.17** |
| **UC256** | ✅ | ✅ | — | — | — | ✅ | I01 | (Đã phân tích v5) |
| **UC257** | — | — | — | — | — | ✅ | — | Toast/Dialog bỏ dấu `.` — **Đã sửa v2.13** |

---

## L. ƯU TIÊN XỬ LÝ (v6)

### 🔴 Ưu tiên cao — Ảnh hưởng logic / UX
1. **UC249, UC250** — Nút "Lưu thay đổi" Disabled → Luôn Enabled (I01)
2. **UC251** — Nút "Cập nhật mật khẩu" Disabled → Luôn Enabled (I01)
3. **UC53** — Nút "Gửi phản ánh" Disabled → Luôn Enabled (I01)
4. **UC53, UC249, UC250** — Max length các trường về rule chung (255/3000)
5. **UC42-44** — Search max 500 → 255 (E05)

### 🟡 Ưu tiên trung bình — Error message format
4. **UC53** — Sửa placeholder; bỏ `...` ở format validation errors
5. **UC251** — Bỏ `.` trong format validation errors (sai định dạng MK, không trùng khớp, bị khóa)
6. **UC249** — Sửa format error vượt max length (H03 format)
7. **UC45-51** — Date validation: thêm `!`

---

## M. NGOẠI LỆ ĐÃ XÁC NHẬN (EXCEPTIONS)

Các case sau đây đi ngược lại với rule chung của CMR nhưng đã được phê duyệt làm **Ngoại lệ (Exception)**, không cần sửa lại theo CMR:
1. **Mã bưu chính (UC249, UC250):** Cho phép nhập freetext, không giới hạn độ dài, không chặn ký tự đặc biệt (Ngoại lệ cho Mục A, Mục B).
2. **Error Message tùy chỉnh (UC249, UC250, UC252):** Cho phép customize các error message rỗng để khớp với Web (VD: *"Vui lòng nhập địa chỉ email"*, *"Vui lòng nhập họ và tên người đại diện"*, *"Vui lòng nhập mã định danh người đại diện"*) thay vì bám cứng format `"Vui lòng nhập [tên trường]"`.
3. **Placeholder Ô tìm kiếm (UC87):** Cho phép giữ nguyên *"Tìm kiếm nhanh theo tên dự án"* thay vì *"Nhập [tên trường]"*.
4. **Kill app luôn logout (CMR-18):** Đã cập nhật lại file `CMR_Mobile.md` (v1.10) thành "Xóa session, yêu cầu đăng nhập lại" thay vì giữ session.

---

*Kết thúc v6.2 — Full scan 38 UC SRS-mobile.*
*Tất cả Pending BA đã resolved. Lỗi hệ thống/empty state: giữ nguyên, không cập nhật SRS.*

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-21 | v6.0 → v6.1 | Mục E — Phân tích ảnh hưởng Search Box | (Không có UC76-82) | Bổ sung: UC76-82 — Ô tìm kiếm FAQ, Max 500 → 255 | Review chéo phát hiện CMR bỏ sót UC76-82 |
| 2026-05-21 | v6.0 → v6.1 | Mục K — Ma trận UC | (Không có UC76-82, UC83-86) | Bổ sung 2 dòng: UC76-82 (E05, H) và UC83-86 (H) | Review chéo phát hiện ma trận thiếu tracking |
| 2026-05-22 | v6.1 → v6.2 | Mục B — Trường Mã (Code field) | Chỉ cập nhật Rule B05 chung chung | Bổ sung yêu cầu update độ dài cụ thể: Cá nhân đúng 12 số, DN đúng 10 số | Theo rule mới nhất |
| 2026-05-21 | v6.0 → v6.1 | Ma trận K — Cột H (Error `.`), dòng UC58 | `✅` | `—` | UC58 không có inline validation error (chỉ system error/empty state). Đánh dấu ✅ là sai — sửa lại thành `—`. |
