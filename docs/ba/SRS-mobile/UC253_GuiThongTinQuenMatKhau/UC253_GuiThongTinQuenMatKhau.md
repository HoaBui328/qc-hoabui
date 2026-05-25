# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC253 — Gửi thông tin quên mật khẩu trên Mobile
**Ngày tạo:** 13/05/2026
**Ngày cập nhật:** 14/05/2026
**Phiên bản:** v2.6
**Cập nhật:** 19/05/2026 — v2.3: Đồng bộ error message mật khẩu sai định dạng với UC252/UC251.

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Quản lý tài khoản |
| Đối tượng thực hiện | Người dùng vãng lai (Chưa đăng nhập) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 13/05/2026 |
| Phiên bản | v2.6 |

---

## UC253 — Gửi thông tin quên mật khẩu trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Gửi thông tin quên mật khẩu
- **Mô tả:** Chức năng cho phép người dùng khôi phục lại quyền truy cập vào tài khoản khi quên mật khẩu đăng nhập, thông qua email đã đăng ký.
- **Phân quyền:** Không yêu cầu đăng nhập.
- **Phạm vi ngoài UC (Exclusions):** Đổi mật khẩu chủ động (UC251) không thuộc tài liệu này.
- **Truy cập chức năng:** Màn hình Đăng nhập → Tap **"Quên mật khẩu?"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Mật khẩu mới được thiết lập và ghi nhận vào DB; toàn bộ token cũ bị invalidate.
- **Chức năng đáp ứng usecase số:** UC253 (Phụ lục XIV)
- **Ngôn ngữ mặc định:** Tiếng Việt (→ CMR-17; do người dùng chưa đăng nhập, dùng ngôn ngữ mặc định của ứng dụng).

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Quên mật khẩu

**Mô tả giao diện:**
Nền đỏ toàn màn hình. Card trắng bo góc chứa subtitle, tiêu đề, mô tả, form nhập Mã định danh, nút Gửi email và link Quay lại đăng nhập. Nút Back (←) cố định góc trên trái ngoài card.

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Nút Back (←) | Icon Button | | **Quy tắc hiển thị:** Nằm trên nền đỏ, góc trái trên cùng (ngoài card trắng).<br>**Quy tắc hành động:** Tap → Điều hướng về màn hình Đăng nhập. |
| 2 | Subtitle | Label | | **Quy tắc hiển thị:** Nằm trên cùng trong card, chữ nhỏ, màu xám. Nội dung: **"CỔNG MỘT CỬA ĐẦU TƯ QUỐC GIA HỖ TRỢ KHÔI PHỤC"**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |
| 3 | Tiêu đề chính | Label | | **Quy tắc hiển thị:** Font to, đậm. Nội dung: **"Quên mật khẩu?"**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |
| 4 | Mô tả hướng dẫn | Label | | **Quy tắc hiển thị:** Font nhỏ hơn tiêu đề, màu xám. Nội dung: **"Vui lòng nhập mã định danh bạn đã đăng ký. Chúng tôi sẽ gửi đường dẫn khởi tạo mật khẩu mới vào email của bạn."**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |
| 5 | Mã định danh | Textbox | ✱ | **Quy tắc hiển thị:** Label **"Mã định danh *"**. Placeholder: **"Nhập mã định danh"**. Bàn phím: **Numeric**. Max length: **50 ký tự**.<br>**Quy tắc hành động:** Tap → Mở bàn phím numeric. Hệ thống auto-trim khoảng trắng đầu/cuối trước khi validate (CMR-09).<br>**Validation** *(on-blur — hiển thị lỗi ngay khi rời khỏi trường)*:<br>- Để trống hoặc chỉ khoảng trắng → *"Vui lòng nhập Mã định danh"*<br>- Nhập ký tự không hợp lệ → *"Mã không bao gồm khoảng trắng và ký tự có dấu"* |
| 6 | Gửi email | Button (Primary) | | **Quy tắc hiển thị:** Nền đỏ đậm, text trắng.<br>- **Luôn Enabled** (nền đỏ). Không có trạng thái Disabled (CMR-09).<br>**Quy tắc hành động:** Tap (có debounce — CMR-18) → Hiển thị loading overlay → Gọi API kiểm tra Mã định danh và gửi email:<br>- **Thành công:** Toast *"Đường dẫn đặt lại mật khẩu đã được gửi đến email của bạn."*<br>- **Mã định danh không tồn tại:** Toast/Inline error: *"Mã định danh không tồn tại trên hệ thống."*<br>- **Timeout (>10s):** Toast *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + Nút "Thử lại". (CMR-07, CMR-16)<br>- **Mất mạng:** Toast *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + Nút "Thử lại". (CMR-07)<br>- **Lỗi 5xx:** Toast *"Hệ thống đang bận. Vui lòng thử lại sau."* (CMR-07) |
| 7 | Quay lại đăng nhập | Link (Text Red) | | **Quy tắc hiển thị:** Màu đỏ, nằm dưới nút Gửi email.<br>**Quy tắc hành động:** Tap → Điều hướng về màn hình Đăng nhập. |

---

#### 2.2 Màn hình Đặt lại mật khẩu

**Mô tả giao diện:**
Màn hình này được mở ra từ Deep link trong Email khôi phục mật khẩu. Nền đỏ toàn màn hình. Card trắng bo góc chứa subtitle, tiêu đề, mô tả, form đặt lại mật khẩu, nút submit và link Quay lại đăng nhập. Footer text nằm dưới card.

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Nút Back (←) | Icon Button | | **Quy tắc hiển thị:** Nằm trên nền đỏ, góc trái trên cùng (ngoài card trắng).<br>**Quy tắc hành động:** Tap → Điều hướng về màn hình Đăng nhập. |
| 2 | Subtitle | Label | | **Quy tắc hiển thị:** Nằm trên cùng trong card, chữ nhỏ, màu xám. Nội dung: **"CỔNG MỘT CỬA ĐẦU TƯ QUỐC GIA HỖ TRỢ ĐẶT LẠI MẬT KHẨU"**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |
| 3 | Tiêu đề chính | Label | | **Quy tắc hiển thị:** Font to, đậm. Nội dung: **"Đặt lại mật khẩu"**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |
| 4 | Mô tả hướng dẫn | Label | | **Quy tắc hiển thị:** Font nhỏ hơn tiêu đề, màu xám. Nội dung: **"Nhập mật khẩu mới để tiếp tục sử dụng hệ thống."**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |
| 5 | Mật khẩu mới | Password Input | ✱ | **Quy tắc hiển thị:** Label **"Mật khẩu mới *"**. Placeholder: **"Nhập mật khẩu mới"**. Icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Max length: **50 ký tự**.<br>**Quy tắc hành động:** Tap icon mắt gạch chéo → Hiện mật khẩu (icon đổi thành mắt thường). Tap lại → Ẩn mật khẩu. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br>**Validation** *(on-blur)*:<br>- Để trống → *"Vui lòng nhập Mật khẩu mới"*<br>- Nhập quá 50 ký tự → *"Mật khẩu không được vượt quá 50 ký tự!"*<br>- Không đủ độ phức tạp (< 8 ký tự, thiếu Hoa/Thường/Số) → *"Mật khẩu phải từ 8 ký tự, chứa ít nhất 1 chữ hoa, 1 chữ thường và 1 chữ số"* |
| 6 | Nhập lại mật khẩu | Password Input | ✱ | **Quy tắc hiển thị:** Label **"Nhập lại mật khẩu *"**. Placeholder: **"Nhập lại mật khẩu"**. Icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Max length: **50 ký tự**.<br>**Quy tắc hành động:** Tap icon mắt gạch chéo → Hiện mật khẩu. Tap lại → Ẩn. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br>**Validation** *(on-blur)*:<br>- Để trống → *"Vui lòng nhập lại mật khẩu"*<br>- Nhập quá 50 ký tự → *"Mật khẩu không được vượt quá 50 ký tự!"*<br>- Không khớp với Mật khẩu mới → *"Mật khẩu nhập lại không khớp. Vui lòng kiểm tra lại"* |
| 7 | Đặt lại mật khẩu | Button (Primary) | | **Quy tắc hiển thị:** Nền đỏ đậm, text trắng.<br>- **Luôn Enabled** (nền đỏ). Không có trạng thái Disabled (CMR-09).<br>**Quy tắc hành động:** Tap (có debounce — CMR-18) → Hiển thị loading overlay → Gọi API cập nhật mật khẩu:<br>- **Thành công:** Toast *"Cập nhật mật khẩu thành công"* → Invalidate toàn bộ token → Điều hướng về màn hình Đăng nhập.<br>- **Timeout (>10s):** Toast *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + Nút "Thử lại". (CMR-07, CMR-16)<br>- **Mất mạng:** Toast *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + Nút "Thử lại". (CMR-07)<br>- **Lỗi 5xx:** Toast *"Hệ thống đang bận. Vui lòng thử lại sau."* (CMR-07) |
| 8 | Quay lại đăng nhập | Link (Text Red) | | **Quy tắc hiển thị:** Màu đỏ, nằm dưới nút Đặt lại mật khẩu.<br>**Quy tắc hành động:** Tap → Điều hướng về màn hình Đăng nhập. |
| 9 | Footer text | Label | | **Quy tắc hiển thị:** Nằm dưới card, nền đỏ, chữ trắng căn giữa. Nội dung: **"Nhanh, an toàn và bảo mật — sử dụng tài khoản Cổng Một Cửa Đầu Tư Quốc Gia ở mọi dịch vụ."**. Văn bản dài: wrap xuống dòng (không truncate).<br>**Quy tắc hành động:** Không tap được, không có action. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Deep link xác thực

- Link reset mật khẩu qua Email có thời hạn do hệ thống BE cấu hình.
- Click link → Mở thẳng vào App, điều hướng đến màn hình Đặt lại mật khẩu (§2.2).
- **Nếu link đã hết hạn:** App hiển thị Toast: *"Link đặt lại mật khẩu đã hết hạn. Vui lòng thử lại."* → Điều hướng về màn hình Quên mật khẩu (§2.1) để người dùng gửi lại yêu cầu.
- **Nếu mở link trên thiết bị chưa cài app:**
  - **Mobile (iOS / Android):** Điều hướng đến App Store / Google Play để tải app.
  - **PC / Trình duyệt không hỗ trợ deep link:** Mở trang web (web portal) tương ứng.

#### 3.2 Security

- Sau khi Reset password thành công, hệ thống bắt buộc invalidate mọi token hiện tại → Đẩy user ra khỏi App ở mọi thiết bị (force logout).

#### 3.3 Tác động cross-UC: Đăng ký tài khoản (UC252)

> Khi user thực hiện Quên mật khẩu và nhập Mã định danh, hệ thống cần phân biệt 2 trường hợp:

| Case | Điều kiện | Hành vi |
|---|---|---|
| Mã định danh không tồn tại trong DB | Không có record nào khớp | Toast: *"Mã định danh không tồn tại trên hệ thống."* |
| Mã định danh tồn tại nhưng tài khoản **chưa xác thực** | Record có trạng thái "Chưa xác thực" | Toast: *"Tài khoản chưa được xác thực. Vui lòng thực hiện Đăng ký lại để nhận email xác thực mới."* |

> **Lưu ý:** Trạng thái "chưa xác thực" được tạo ra từ luồng Đăng ký (UC252). Bảng trên ghi nhận hành vi của UC253 khi gặp tài khoản ở trạng thái này.

#### 3.4 Đa ngôn ngữ (→ CMR-17)

Toàn bộ text tĩnh trên màn hình (label, placeholder, thông báo lỗi, toast, nút) dịch tự động theo ngôn ngữ mặc định của ứng dụng (5 ngôn ngữ: VI, EN, ZH, JA, KO). Do người dùng chưa đăng nhập, hiển thị theo ngôn ngữ mặc định của app (Tiếng Việt theo CMR-17).

---

### 4. Acceptance Criteria

| # | Tiêu chí | Pass condition |
|---|---|---|
| AC-01 | Nút Gửi email — Disabled | Nút Gửi email luôn Enabled. Tap → validate Mã định danh → nếu trống hoặc lỗi hiển thị inline error. |
| AC-02 | Nút Gửi email — Enabled | Mã định danh hợp lệ → Nút Gửi email Enabled (nền đỏ). |
| AC-03 | Gửi email thành công | Nhập đúng Mã định danh tồn tại trong DB → Submit → Toast *"Đường dẫn đặt lại mật khẩu đã được gửi đến email của bạn."* |
| AC-04 | Gửi email thất bại | Nhập sai Mã định danh → Toast *"Mã định danh không tồn tại trên hệ thống."* |
| AC-05 | Validation on-blur Mã định danh — trống | Rời khỏi trường khi để trống → Inline error *"Vui lòng nhập Mã định danh"* |
| AC-06 | Validation on-blur Mã định danh — ký tự không hợp lệ | Nhập chữ cái/ký tự đặc biệt → Inline error *"Mã không bao gồm khoảng trắng và ký tự có dấu"* |
| AC-07 | Deep link hoạt động | Click link trong email → Mở đúng màn hình Đặt lại mật khẩu (§2.2) trên app. |
| AC-08 | Deep link hết hạn | Click link hết hạn → Toast *"Link đặt lại mật khẩu đã hết hạn. Vui lòng thử lại."* → Chuyển về §2.1. |
| AC-09 | Nút Đặt lại mật khẩu — Disabled | Nút Đặt lại mật khẩu luôn Enabled. Tap → validate toàn bộ form → nếu có lỗi hiển thị inline error. |
| AC-10 | Nút Đặt lại mật khẩu — Enabled | Cả 2 trường hợp lệ và khớp nhau → Nút Enabled (nền đỏ). |
| AC-11 | Toggle ẩn/hiện mật khẩu — mặc định ẩn | Mở màn hình §2.2: cả 2 trường mật khẩu hiển thị icon mắt gạch chéo (ẩn mặc định). |
| AC-12 | Toggle ẩn/hiện mật khẩu — tap | Tap icon mắt gạch chéo → Hiện mật khẩu (icon đổi). Tap lại → Ẩn mật khẩu. |
| AC-13 | Validation mật khẩu sai định dạng | Nhập MK không đủ phức tạp → Inline error *"Mật khẩu phải từ 8 ký tự, chứa ít nhất 1 chữ hoa, 1 chữ thường và 1 chữ số"* |
| AC-14 | Validation mật khẩu không khớp | Nhập lại MK khác MK mới → Inline error *"Mật khẩu nhập lại không khớp. Vui lòng kiểm tra lại"* |
| AC-15 | Đặt lại MK thành công | Nhập 2 MK khớp và đúng định dạng → Submit → Toast *"Cập nhật mật khẩu thành công"* → Logout mọi token cũ → Về màn Login. |
| AC-16 | Timeout | API không phản hồi trong 10s → Toast *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + Nút Thử lại. |
| AC-17 | Mất mạng | Mất kết nối khi submit → Toast *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + Nút Thử lại. |
| AC-18 | Debounce | Double-tap nút submit không trigger 2 lần API (CMR-18). |
| AC-19 | Keyboard Mã định danh | Focus vào trường Mã định danh → Bàn phím ảo loại Numeric. |
| AC-20 | Max length mật khẩu | Nhập ký tự thứ 51 vào trường mật khẩu → Hệ thống không nhận thêm ký tự (gõ phím). Paste vượt quá 50 ký tự → Inline error *"Mật khẩu không được vượt quá 50 ký tự!"* |

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Nội dung cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 13/05/2026 | v1.0 | Khởi tạo tài liệu (Tách từ UC250-253_QuanLyTaiKhoan v3.4). Chuẩn hóa format. | (Không có) | v1.0 cơ bản | |
| 14/05/2026 | v1.0 → v2.0 | Bổ sung UI Object đầy đủ (Subtitle, Title, Desc, Footer); áp dụng CMR-09 (on-blur validation, Disabled/Enabled, auto-trim); áp dụng CMR-07/16 (Loading, Timeout, Mất mạng, Lỗi 5xx); áp dụng CMR-18 (Debounce); sửa icon mặc định mật khẩu từ "hiển thị" → "ẩn" (đồng bộ wireframe); bổ sung inline error text (đồng bộ UC256); chốt deep link hết hạn → Toast + redirect §2.1; bổ sung keyboard type Numeric; bổ sung max length 50 ký tự; làm rõ ngôn ngữ mặc định cho guest (CMR-17); mở rộng AC từ 4 → 20 tiêu chí. | v1.0 | v2.0 | Audit v1 — Q1–Q10 |
| 14/05/2026 | v2.0 → v2.1 | Bổ sung xử lý deep link cross-device: Mobile chưa cài app → Store; PC/browser → web portal. | Chưa có | v2.1 | Audit v2 — N2 |
| 17/05/2026 | v2.1 → v2.2 | CMR-09 — Chuẩn hoá required message (Textbox) | `"Mã định danh là bắt buộc."` | `"Vui lòng nhập Mã định danh"` | Đồng bộ CMR-09 v1.7 |
| 19/05/2026 | v2.2 → v2.3 | Đồng bộ error message mật khẩu sai định dạng | *"Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường và chữ số."* | *"Mật khẩu phải từ 8 ký tự, chứa ít nhất 1 chữ hoa, 1 chữ thường và 1 chữ số"* | Đồng bộ UC252/UC251 |
| 2026-05-21 | v2.3 → v2.4 | Align CMR Mobile v6.0 | 1. Nút "Gửi email" và "Đặt lại MK" Disabled→Luôn Enabled. 2. Bỏ dấu "." cuối inline validation errors. 3. Thêm rule CMR-11 cho Mã định danh. |
| 2026-05-21 | v2.4 → v2.5 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v2.5 → v2.6 | Align CMR Mobile v6.0 | Áp dụng rule Code Field cho Mã định danh (Max length 50, đổi lỗi) và bổ sung lỗi vượt Max length 50 cho Password |
