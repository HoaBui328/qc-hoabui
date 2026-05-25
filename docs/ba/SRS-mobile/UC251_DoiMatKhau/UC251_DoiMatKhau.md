# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC251 — Đổi mật khẩu
**Ngày tạo:** 13/05/2026
**Phiên bản:** v1.12
**Cập nhật:** 2026-05-25 — v1.12: Khôi phục dấu chấm than (!) ở cuối thông báo lỗi max length để đồng bộ chuẩn CMR-09.

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Quản lý tài khoản |
| Đối tượng thực hiện | Cá nhân / Tổ chức (đã đăng nhập) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 13/05/2026 |
| Phiên bản | v1.12 |

---

## UC251 — Đổi mật khẩu trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Đổi mật khẩu
- **Mô tả:** Chức năng cho phép người dùng thay đổi mật khẩu đăng nhập vào ứng dụng.
- **Phân quyền:** Cá nhân / Tổ chức đã đăng nhập.
- **Phạm vi ngoài UC (Exclusions):** Quên mật khẩu (UC253) không thuộc tài liệu này.
- **Truy cập chức năng:** Sidebar → **"Cấu hình tài khoản"** → Tap **"Đổi mật khẩu"**.
- **Điều kiện tiên quyết (Preconditions):** Người dùng đã đăng nhập vào ứng dụng.
- **Điều kiện kết thúc (Postconditions):** Mật khẩu được cập nhật thành công. Đăng xuất tất cả các thiết bị.
- **Chức năng đáp ứng usecase số:** UC251 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Đổi mật khẩu (UC251)

**Mô tả giao diện:**
Form đổi mật khẩu dành cho người dùng đã đăng nhập. App bar có tiêu đề "Đổi mật khẩu" và nút **Back (←)**.

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Nút Back (←) | Icon Button | | **Quy tắc hiển thị:** Nằm trên App Bar.<br>**Quy tắc hành động:** Tap Back → Quay về màn hình trước. Android Hardware Back button hoạt động tương tự. |
| 2 | Mật khẩu hiện tại | Password Input | ✱ | **Quy tắc hiển thị:** Icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Tap icon mắt gạch chéo → Hiện mật khẩu (icon đổi thành mắt thường). Tap lại → Ẩn.<br>**Max length:** 50 ký tự.<br>**Validation** *(ngay khi rời trường)*:<br>- Để trống -> *"Vui lòng nhập Mật khẩu hiện tại!"* |
| 3 | Mật khẩu mới | Password Input | ✱ | **Quy tắc hiển thị:** Icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Tap icon mắt gạch chéo → Hiện mật khẩu. Tap lại → Ẩn.<br>**Max length:** 50 ký tự.<br>**Validation** *(ngay khi rời trường)*:<br>- Để trống -> *"Vui lòng nhập Mật khẩu mới!"*<br>- Gõ/Paste > 50 ký tự -> *"Mật khẩu không được vượt quá 50 ký tự!"* (CMR-09)<br>- Nhập ít hơn 8 ký tự hoặc sai định dạng -> *"Mật khẩu phải từ 8 ký tự, chứa ít nhất 1 chữ hoa, 1 chữ thường và 1 chữ số"*<br>**Validation** *(khi nhấn nút "Cập nhật mật khẩu")*:<br>- Trùng MK cũ -> *"Mật khẩu mới phải khác mật khẩu hiện tại"* (API trả về lỗi, hiển thị inline error ngay dưới trường) |
| 4 | Xác nhận mật khẩu mới | Password Input | ✱ | **Quy tắc hiển thị:** Icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Tap icon mắt gạch chéo → Hiện mật khẩu. Tap lại → Ẩn.<br>**Max length:** 50 ký tự.<br>**Validation** *(ngay khi rời trường)*:<br>- Để trống -> *"Vui lòng nhập Xác nhận mật khẩu"*<br>- Không khớp -> *"Mật khẩu không trùng khớp"* |
| 5 | Cập nhật mật khẩu | Button (Primary) | | **Quy tắc hiển thị:** Luôn Enabled (CMR-09). Không có trạng thái Disabled.<br>**Quy tắc hành động:** Tap -> Nút chuyển sang trạng thái **loading** (spinner, không thể bấm lại) -> Gọi API đổi mật khẩu trực tiếp *(không hiển thị Confirmation Dialog trước khi submit)*. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Đổi mật khẩu
- **Đổi mật khẩu thành công:** Hiển thị Toast: *"Đổi mật khẩu thành công"* -> Hệ thống bắt buộc Invalid mọi token hiện tại -> Đẩy user ra khỏi App ở mọi thiết bị, quay về màn Login. Bộ đếm nhập sai được reset về 0.
- **Confirmation Dialog — Nút Submit:** Không hiển thị Confirmation Dialog khi tap "Cập nhật mật khẩu" — gọi API trực tiếp.
- **Loading State:** Trong khi API đang xử lý, nút "Cập nhật mật khẩu" hiển thị spinner (loading), không thể bấm lại để tránh double-submit.
- **Sai mật khẩu hiện tại (< 5 lần):** API trả lỗi -> Hiển thị inline error ngay dưới trường "Mật khẩu hiện tại": *"Mật khẩu hiện tại không đúng"* Không hiển thị thêm Toast. Bộ đếm nhập sai tăng lên 1.
- **Security Lock — Bị khóa (đủ 5 lần sai):**
  1. Hiển thị Toast: *"Tài khoản của bạn đã bị khóa tạm thời. Vui lòng thử lại sau 15 phút."*
  2. Hệ thống Invalid token hiện tại -> Đẩy user ra khỏi App, quay về màn hình Đăng nhập.
  3. Trong 15 phút tiếp theo, nếu user cố đăng nhập lại: hiển thị Toast *"Tài khoản của bạn đã bị khóa tạm thời. Vui lòng thử lại sau 15 phút."* và không cho tiến hành đăng nhập.
  4. Sau 15 phút: tài khoản tự mở khóa, bộ đếm nhập sai reset về 0.
- **Error Flows API:** Mất mạng/Timeout/5xx → Hiển thị Toast lỗi theo CMR-07.

#### 3.2 Đa ngôn ngữ (CMR-17)
Toàn bộ text tĩnh trên màn hình (header, label, placeholder, error message inline, toast text) dịch tự động theo 5 ngôn ngữ: VI, EN, ZH, JA, KO dựa trên cấu hình App.

---

### 4. Acceptance Criteria

| # | Tiêu chí | Pass condition |
|---|---|---|
| AC-01 | Đổi mật khẩu thành công | Nhập đúng MK cũ, 2 MK mới khớp -> Toast *"Đổi mật khẩu thành công"* -> Logout toàn bộ thiết bị. Bộ đếm nhập sai reset về 0. |
| AC-02 | Inline error sai MK cũ | Nhập sai MK cũ (< 5 lần) -> Hiển thị inline error *"Mật khẩu hiện tại không đúng"* ngay dưới trường. Không hiển thị Toast phụ. |
| AC-03 | Security Lock — bị khóa | Nhập sai MK cũ đủ 5 lần -> Toast *"Tài khoản của bạn đã bị khóa tạm thời. Vui lòng thử lại sau 15 phút."* -> Token bị invalid -> Bị đẩy ra màn Login. Không thể thực hiện đổi mật khẩu cho đến khi hết thời gian khóa. |
| AC-04 | Security Lock — cố login lại khi đang khóa | Trong 15 phút bị khóa, thử đăng nhập -> hiện Toast tương tự, không cho tiến hành login. |
| AC-05 | Security Lock — tự mở khóa | Sau 15 phút: tài khoản tự mở khóa, bộ đếm nhập sai reset về 0. |
| AC-06 | Validation mật khẩu mới | Báo lỗi inline nếu MK mới không đúng rule độ phức tạp hoặc trùng MK cũ. |
| AC-07 | Button CMR-09 | Nút "Cập nhật mật khẩu" luôn Enabled. Tap → validate toàn bộ form → nếu có lỗi hiển thị inline error, nếu hợp lệ gọi API. |
| AC-08 | Max length password | Gõ hoặc paste > 50 ký tự -> hiển thị inline error *"Mật khẩu không được vượt quá 50 ký tự!"* (CMR-09). |
| AC-09 | Loading state | Sau khi tap nút, nút chuyển sang trạng thái loading; không thể bấm lại cho đến khi API trả về kết quả. |
| AC-10 | Format Inline Error | Lỗi hiển thị ngay dưới trường khi focus out, text hiển thị đúng chuẩn. |
| AC-11 | Back | Tap Back (bất kể trạng thái) → quay về màn hình trước. Android Hardware Back hoạt động tương tự. |
| AC-12 | Toggle ẩn/hiện mật khẩu — mặc định ẩn | Mở màn hình: cả 3 trường mật khẩu hiển thị icon mắt gạch chéo (ẩn mặc định). Tap icon → Hiện (icon đổi thành mắt thường). Tap lại → Ẩn. |

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Nội dung cập nhật |
|---|---|---|
| 13/05/2026 | v1.0 | Khởi tạo tài liệu (Tách từ UC250-253_QuanLyTaiKhoan v3.4). Chuẩn hóa format. |
| 14/05/2026 | v1.1 | Cập nhật theo Q&A BA (Q1–Q5): Nút disabled khi form invalid (CMR-09); Toast text "Đổi mật khẩu thành công"; Max length 50 ký tự cho tất cả trường password; Nút loading state khi API đang xử lý. |
| 14/05/2026 | v1.2 | Cập nhật theo Q&A BA (Q6–Q7): Sai MK cũ < 5 lần → inline error (không toast phụ); Security Lock đầy đủ (toast text, redirect Login, block login 15 phút, auto-unlock). Bổ sung reset bộ đếm sau thành công. Tái cấu trúc AC-01→AC-10. |
| 14/05/2026 | v1.3 | Sửa AC-03 đúng ngữ cảnh đổi MK (bị redirect về Login, không thể đổi MK). Thêm Q8 open question. |
| 14/05/2026 | v1.4 | Bổ sung AC-11 (Back button). Fix conflict "Confirmation Dialog" trong Section 3.1. |
| 14/05/2026 | v1.5 | Validation "Trùng MK cũ": chuyển từ on-blur sang on-submit (API trả về lỗi, hiển thị inline error). Giải quyết gap kỹ thuật client-side. |
| 14/05/2026 | v1.6 | Đồng bộ mặc định icon mắt cả 3 trường mật khẩu từ "mặc định xem được" → "mặc định ẩn" (khớp UC253). Bổ sung AC-12. |
| 2026-05-21 | v1.6 → v1.7 | Align CMR Mobile v6.0 | 1. Nút "Cập nhật mật khẩu" Disabled→Luôn Enabled. 2. Bỏ dấu "." cuối inline validation errors. |
| 2026-05-21 | v1.7 → v1.8 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v1.8 → v1.9 | Align CMR-09 — Fix error Mật khẩu max length | §2.1 #3 (dòng 45) và AC-08 (dòng 81): `"Mật khẩu nhập quá ký tự cho phép"` → `"Mật khẩu không được vượt quá 50 ký tự"` (CMR-09). |
| 2026-05-25 | v1.9 → v1.10 | Đồng nhất rule max length mật khẩu | Gộp rule: Gõ hoặc paste > 50 ký tự đều hiển thị inline error (bỏ block input) để thống nhất theo CMR-09. |
| 2026-05-25 | v1.10 → v1.11 | Update message lỗi max length | Thông báo lỗi `"Mật khẩu không được vượt quá 50 ký tự!"` | Bỏ dấu chấm than ở cuối: `"Mật khẩu không được vượt quá 50 ký tự"` |
| 2026-05-25 | v1.11 → v1.12 | Khôi phục dấu chấm than | `"Mật khẩu không được vượt quá 50 ký tự"` | Khôi phục lại dấu `!` thành `"Mật khẩu không được vượt quá 50 ký tự!"` để đồng bộ đúng chuẩn CMR-09 |
