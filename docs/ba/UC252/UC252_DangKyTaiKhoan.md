# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC252 — Đăng ký tài khoản trên Mobile
**Ngày tạo:** 13/05/2026
**Phiên bản:** v2.5
**Cập nhật:** 19/05/2026 — v2.5: Mã định danh Tổ chức/DN: bỏ rule min 10 số, chỉ giữ max 12 chữ số.

| Thuộc tính              | Giá trị                                    |
| ------------------------- | -------------------------------------------- |
| BA phụ trách            | huy.lai2                                     |
| Phân hệ                 | Ứng dụng Di động (Mobile App)            |
| Loại chức năng         | Quản lý tài khoản                        |
| Đối tượng thực hiện | Người dùng vãng lai (Chưa đăng nhập) |
| Giao diện                | Màn hình Mobile (Portrait)                 |
| Ngày tạo                | 13/05/2026                                   |
| Phiên bản               | v2.5                                         |

---

## UC252 — Đăng ký tài khoản trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Đăng ký tài khoản
- **Mô tả:** Chức năng cho phép người dùng đăng ký mới một tài khoản để sử dụng hệ thống. Người dùng có thể chọn 1 trong 3 loại: Cá nhân Việt Nam, Cá nhân nước ngoài, hoặc Tổ chức / Doanh nghiệp.
- **Phân quyền:** Không yêu cầu đăng nhập.
- **Phạm vi ngoài UC (Exclusions):** Đăng ký bằng tài khoản mạng xã hội (Google, Facebook, ...) **không** thuộc phạm vi UC này.
- **Truy cập chức năng:** Màn hình Đăng nhập → Tap **"Đăng ký"**.
- **Điều kiện tiên quyết (Preconditions):** Không có.
- **Điều kiện kết thúc (Postconditions):** Đăng ký thành công, gửi email xác thực. Sau khi xác thực, tài khoản được kích hoạt trên hệ thống.
- **Chức năng đáp ứng usecase số:** UC252 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Bước 1: Chọn loại tài khoản

**Mô tả giao diện:**
Màn hình đầu tiên của luồng Đăng ký. Giao diện có App Bar, Step Indicator (1 Chọn loại - 2 Thông tin), và danh sách các loại tài khoản để người dùng chọn. Người dùng chạm vào một tùy chọn để chuyển sang Bước 2.

- **Cá nhân Việt Nam:** Đăng ký bằng CCCD/Số định danh.
- **Tổ chức / Doanh nghiệp:** Đăng ký bằng mã số doanh nghiệp.
- **Cá nhân nước ngoài:** Đăng ký bằng **Hộ chiếu** (Passport). *(Lưu ý: flow này được bàn giao sau cùng — thuộc phạm vi **UC255**.)*

---

#### 2.2 Bước 2: Form Đăng ký

**Mô tả giao diện:**
Form bao gồm các trường định danh, liên hệ và mật khẩu.

**App Bar:**

| # | Thành phần   | Kiểu       | Mô tả/Ghi chú                                                                                                                                                                                                                   |
| - | -------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nút Back (←) | Icon Button | **Quy tắc hiển thị:** Luôn hiển thị ở góc trái.`<br>`**Quy tắc hành động:** Tap → Quay về **Bước 1 (Chọn loại tài khoản)**.                                                               |
| 2 | Tiêu đề     | Label       | **Quy tắc hiển thị:**`<br>`- **Cá nhân VN & Cá nhân NN:** Cố định *"Đăng ký tài khoản cá nhân"`.`<br>`- **Tổ chức / Doanh nghiệp:** Cố định *"Đăng ký tài khoản tổ chức"*. |

**Section "Thông tin cá nhân / Tổ chức":**

| # | Tên trường                 | Kiểu trường | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ----------------------------- | -------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Tên tổ chức / Họ và tên | Textbox        | ✱         | **Quy tắc hiển thị:**`<br>`- Nếu chọn Cá nhân: Hiển thị nhãn **"Họ và tên*".`<br>`- Nếu chọn Tổ chức: Hiển thị nhãn **"Tên tổ chức*"**.`<br>`- Placeholder: *"Nhập Họ và tên"* / *"Nhập Tên tổ chức"* tùy loại tài khoản.`<br>`**Quy tắc hành động:** Auto-trim khoảng trắng đầu/cuối (CMR-09).`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Họ và tên"* hoặc *"Vui lòng nhập Tên tổ chức"* tùy loại.`<br>`- Nhập quá 50 ký tự → *"Họ và tên nhập quá ký tự cho phép"* / *"Tên tổ chức nhập quá ký tự cho phép"* tùy loại.                                                                     |
| 2 | Mã định danh               | Textbox        | ✱         | **Quy tắc hiển thị:** Có icon 💳. Placeholder: *"Nhập Mã định danh"*. Không chấp nhận dấu space (theo CMR-11).`<br>`**Quy tắc hành vi (theo loại tài khoản):**`<br>`- **Cá nhân Việt Nam (CCCD/CMND):** Chỉ chấp nhận ký tự số (0–9). Độ dài bắt buộc: **12 chữ số**. Nếu nhập quá 12 số → *"Mã định danh nhập quá ký tự cho phép"*. Nếu ít hơn 12 số → *"Mã định danh nhập chưa đủ ký tự cho phép"*`<br>`- **Tổ chức / Doanh nghiệp:** Chỉ chấp nhận ký tự số. Max 12 chữ số. Nếu nhập quá 12 số → *"Mã định danh nhập quá ký tự cho phép"*`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Mã định danh"*`<br>`- Nhập ký tự không phải số → *"Mã định danh chỉ gồm các số 0-9."* |
| 3 | Ngày cấp                    | Datepicker     | ✱         | **Quy tắc hiển thị:** Định dạng dd/MM/yyyy. Có icon 📅.`<br>`**Quy tắc hành động:** Tap mở Datepicker. Max date: hôm nay. Min date: 01/01/1900. Ngày ngoài khoảng bị disable.`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Chưa chọn → *"Vui lòng chọn Ngày cấp"*                                                                                                                                                                                                                                                     |
| 4 | Nơi cấp                     | Textbox        | ✱         | **Quy tắc hiển thị:** Có icon 📍. Placeholder: *"Nhập Nơi cấp"*. Auto-trim khoảng trắng đầu/cuối (CMR-09). **Max length: 500 ký tự** (CMR-11).`<br>`**Quy tắc hành động:** Nhập tự do.`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Nơi cấp"*`<br>`- Nhập quá 500 ký tự → *"Nơi cấp nhập quá ký tự cho phép"*                                                                                                                                                      |
| 5 | Mã số thuế                 | Textbox        | ✱         | **Quy tắc hiển thị:** Bắt buộc với Tổ chức và Cá nhân VN. (Ẩn đối với Cá nhân NN). Placeholder: *"Nhập Mã số thuế"*.`<br>`**Quy tắc hành động:** Chỉ nhập số.`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Mã số thuế"*`<br>`- **Cá nhân VN:** Nhập ít hơn 10 số → *"Mã số thuế nhập chưa đủ ký tự cho phép"*. Nhập nhiều hơn 10 số → *"Mã số thuế nhập quá ký tự cho phép"*`<br>`- **Tổ chức/DN:** Nhập ít hơn 10 số → *"Mã số thuế nhập chưa đủ ký tự cho phép"*. Nhập nhiều hơn 13 số → *"Mã số thuế nhập quá ký tự cho phép"*                                                  |

**Section "Thông tin liên hệ":**

| # | Tên trường     | Kiểu trường  | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ----------------- | --------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Số điện thoại | Textbox (tel)   | ✱         | **Quy tắc hiển thị:** Ô prefix có dropdown cờ quốc gia (list load từ API, **không có ô tìm kiếm**). Mặc định: 🇻🇳 +84. Ô kế bên nhập số.`<br>`- **Lưu ý:** Nếu luồng đăng ký là "Cá nhân Việt Nam" hoặc "Tổ chức/Doanh nghiệp (VN)", dropdown cờ bị **disabled** (khóa cứng ở +84 Việt Nam, không cho đổi).`<br>`**Quy tắc hành vi:** Chỉ nhập ký tự số (0–9). Không chấp nhận dấu space (theo CMR-11).`<br>`- Với prefix **+84** (VN): đầu số hợp lệ 03/05/07/08/09, đúng **9 chữ số**.`<br>`- Với prefix **quốc gia khác** (Cá nhân NN): áp dụng chuẩn E.164, độ dài linh hoạt từ **6 đến 15 chữ số**.`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Số điện thoại"*`<br>`- Prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ."*`<br>`- Nhập chưa đủ ký tự cho phép → *"Số điện thoại nhập chưa đủ ký tự cho phép"*`<br>`- Nhập quá ký tự cho phép → *"Số điện thoại nhập quá ký tự cho phép"* |
| 2 | Email             | Textbox (email) | ✱         | **Quy tắc hiển thị:** Email keyboard. Placeholder: *"Nhập Email"*. **Max length: 100 ký tự** (CMR-11).`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Email"*`<br>`- Nhập quá 100 ký tự → *"Email nhập quá ký tự cho phép"*`<br>`- Sai định dạng → *"Email không đúng định dạng"*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**Section "Tạo mật khẩu":**

| # | Tên trường         | Kiểu trường | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------- | -------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Mật khẩu            | Password Input | ✱         | **Quy tắc hiển thị:** Có icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Tối đa **50 ký tự**.`<br>`**Quy tắc hành vi:** Tap icon mắt gạch chéo → Hiện mật khẩu (icon đổi thành mắt thường). Tap lại → Ẩn mật khẩu. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập Mật khẩu"*`<br>`- Sai định dạng → *"Mật khẩu phải từ 8 ký tự, chứa ít nhất 1 chữ hoa, 1 chữ thường và 1 chữ số."*`<br>`- Nhập quá 50 ký tự → *"Mật khẩu nhập quá ký tự cho phép"* |
| 2 | Nhập lại mật khẩu | Password Input | ✱         | **Quy tắc hiển thị:** Icon mắt gạch chéo bên phải **(mặc định ẩn — hidden)**. Tối đa **50 ký tự**.`<br>`**Quy tắc hành vi:** Tap icon mắt gạch chéo → Hiện mật khẩu. Tap lại → Ẩn. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).`<br>`**Validation** *(ngay khi rời trường)*:`<br>`- Để trống → *"Vui lòng nhập lại mật khẩu"*`<br>`- Không khớp → *"Mật khẩu không trùng khớp."*                                                                                                                                                                                                                 |

**Khu vực Button (Sticky bottom):**

| # | Tên nút               | Kiểu    | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Đồng ý Điều khoản | Checkbox | **Quy tắc hiển thị:** "Tôi đồng ý với [Điều khoản sử dụng] và [Chính sách bảo mật] của hệ thống".`<br>`**Quy tắc hành vi:** Mặc định chưa check. Các link chữ đỏ mở màn hình quy định (UC83-86). Form data được giữ nguyên khi quay lại.                                                                                                                                                    |
| 2 | Đăng ký tài khoản  | Button   | **Quy tắc hiển thị:**`<br>`- **Disabled** (nền xám, không tương tác) khi: (1) checkbox chưa được đánh dấu, HOẶC (2) bất kỳ trường bắt buộc nào trống hoặc có lỗi validation (CMR-09).`<br>`- **Enabled** (nền đỏ) khi: checkbox đã check **VÀ** toàn bộ form hợp lệ.`<br>`- Có **loading spinner** khi đang gọi API (CMR-07).`<br>`**Quy tắc hành vi:** Tap (khi Enabled, có debounce — CMR-18) → Validate toàn bộ form → Gọi API. Double-tap không trigger 2 lần API.`<br>`**Quy tắc hiển thị khi keyboard:** Khi keyboard hiện lên, sticky bottom có thể bị che. Người dùng có thể scroll để xem nút đăng ký. |

---

#### 2.3 Màn hình Thông báo xác thực tài khoản

Màn hình popup trắng hiển thị sau khi nhấn Đăng ký và API trả về thành công.

| # | Thành phần        | Kiểu              | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nội dung           | Label              | **Quy tắc hiển thị:** *"Hệ thống đã gửi thông báo qua email, vui lòng kiểm tra email để xác thực tài khoản."* Văn bản dài: wrap xuống dòng (không truncate).`<br>`**Quy tắc hành động:** Không tap được, không có action.                                                                                                                                      |
| 2 | Gửi lại email     | Button (Secondary) | **Quy tắc hiển thị:** Hiển thị bên dưới nội dung thông báo.`<br>`**Quy tắc hành động:** Tap → Gọi API gửi lại email xác thực. **Không giới hạn số lần gửi lại.**`<br>`- Thành công: Toast *"Email xác thực đã được gửi lại."*`<br>`- Thất bại (SMTP/mạng): Toast *"Không thể gửi email xác thực. Vui lòng thử lại sau."* (CMR-07). |
| 3 | App Bar / Nút Back | Icon Button        | **Quy tắc hiển thị:** Nút Back (←) ở App Bar hoặc phím Back (Android).`<br>`**Quy tắc hành động:** Tap → **Điều hướng về màn hình Đăng nhập ban đầu**.                                                                                                                                                |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Kiểm tra trùng lặp

Khi nhấn "Đăng ký", hệ thống gọi API. Nếu thông tin đã tồn tại, báo lỗi inline ngay dưới **tất cả** trường bị trùng (không chỉ trường đầu tiên):

- Trùng Email: inline error *"Email đã được đăng ký."* hiển thị ngay dưới trường Email.
- Trùng SĐT: inline error *"Số điện thoại đã được đăng ký."* hiển thị ngay dưới trường SĐT.
- Trùng Mã định danh: inline error *"Mã định danh đã được đăng ký."* hiển thị ngay dưới trường Mã định danh.
- **Nếu API trả về nhiều lỗi trùng đồng thời** (VD: Email + SĐT + Mã định danh): tất cả inline error hiển thị cùng lúc, không ưu tiên theo thứ tự.

#### 3.2 Xác thực tài khoản từ link Email

- Nội dung email được cấu hình từ phía Backend (BE). Link xác thực trong email có thời hạn **sau 1 ngày** sẽ hết hạn.
- **Click link:** Chuyển hướng (Deep link) về ứng dụng Mobile.
- **Xác thực thành công:** Hiển thị màn hình trắng thông báo thành công kèm nút **"Đăng nhập"**. Click nút này → Redirect về màn hình Đăng nhập.
- **Link hết hạn (>1 ngày):** App redirect về ứng dụng và hiển thị Toast: *"Link xác thực đã hết hạn, vui lòng thử lại."* → Điều hướng về màn hình Đăng nhập để người dùng thực hiện lại luồng đăng ký.
- **Link token không hợp lệ:** Redirect về màn hình Đăng nhập → hiển thị Toast: *"Nội dung không tồn tại hoặc đã bị xóa."* (theo CMR-07).
- **Email gửi thất bại (SMTP error, inbox full, spam filter):** Nếu hệ thống không thể gửi email **sau khi đăng ký thành công** → vẫn điều hướng vào màn hình §2.3, đồng thời hiển thị Toast: *"Không thể gửi email xác thực. Vui lòng thử lại."* (CMR-07). Người dùng có thể tap **"Gửi lại email"** tại §2.3 để yêu cầu gửi lại.
- **Gửi lại email xác thực:** Xem §2.3 — Button "Gửi lại email". Không giới hạn số lần. Feedback kết quả qua toast (thành công / thất bại).
- **Step 2 → Tap Back → Step 1:** Selected tile (loại tài khoản đã chọn) được **giữ nguyên** khi quay về Bước 1.

#### 3.3 Đa ngôn ngữ (CMR-17)

Toàn bộ text tĩnh trên màn hình dịch tự động theo 5 ngôn ngữ: VI, EN, ZH, JA, KO dựa trên cấu hình App.

#### 3.4 Xử lý lỗi API (CMR-07, CMR-16)

- **Timeout API (10 giây):** Nếu API không phản hồi trong 10 giây → Hiển thị thông báo: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* Kèm nút "Thử lại" (theo CMR-16).
- **Lỗi mạng:** Hiển thị: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* Kèm nút "Thử lại" (theo CMR-07).
- **Lỗi 500:** Hiển thị: *"Hệ thống đang bận. Vui lòng thử lại sau."* (theo CMR-07).

---

### 4. Acceptance Criteria

| #     | Tiêu chí                                            | Pass condition                                                                                                                                                                                                                     |
| ----- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | Đăng ký thành công                               | Form valid + checkbox checked → Submit → Nhận được màn hình "Đăng ký thành công" và Email xác thực gửi đến địa chỉ đã nhập.                                                                               |
| AC-02 | Format Inline Error                                   | Lỗi hiển thị ngay dưới trường khi focus out, text hiển thị đúng chuẩn.                                                                                                                                                 |
| AC-03 | Lỗi trùng lặp — từng trường                    | Hệ thống báo inline error đúng trường bị trùng (SĐT, Email, Mã định danh) khi submit.                                                                                                                                 |
| AC-04 | Lỗi trùng lặp — nhiều trường đồng thời      | API trả về Email + SĐT + Mã định danh đều trùng → Tất cả 3 inline error hiển thị đồng thời, không chỉ trường đầu tiên.                                                                                     |
| AC-05 | Logic Datepicker                                      | Không cho phép chọn ngày cấp lớn hơn ngày hiện tại hoặc trước năm 1900.                                                                                                                                              |
| AC-06 | Nút Đăng ký — Disabled (chưa check)             | Nút Đăng ký phải bị disabled khi người dùng chưa check vào box Đồng ý Điều khoản (dù form đã hợp lệ).                                                                                                        |
| AC-07 | Nút Đăng ký — Disabled (form lỗi)               | Nút Đăng ký phải bị disabled khi form còn bất kỳ lỗi validation nào (dù đã check checkbox).                                                                                                                          |
| AC-08 | Nút Đăng ký — Enabled                            | Nút Đăng ký chỉ Enabled khi checkbox đã check**VÀ** toàn bộ form hợp lệ.                                                                                                                                         |
| AC-09 | Debounce nút Đăng ký                              | Double-tap nút Đăng ký không tạo 2 API request (CMR-18).                                                                                                                                                                     |
| AC-10 | Mật khẩu mặc định ẩn                            | Mở màn hình form đăng ký: cả 2 trường mật khẩu hiển thị icon mắt gạch chéo (ẩn mặc định).                                                                                                                      |
| AC-11 | Toggle ẩn/hiện mật khẩu                           | Tap icon mắt gạch chéo → Hiện mật khẩu (icon đổi). Tap lại → Ẩn mật khẩu.                                                                                                                                            |
| AC-12 | Xác thực email E2E — thành công                  | Click link xác thực trong email (còn hạn) → App mở màn hình thành công với nút "Đăng nhập".                                                                                                                         |
| AC-13 | Link xác thực hết hạn                             | Click link hết hạn (>1 ngày) → Toast*"Link xác thực đã hết hạn, vui lòng thử lại."* → Chuyển về màn Đăng nhập.                                                                                               |
| AC-14 | Gửi lại email xác thực                            | Tap "Gửi lại email" từ màn hình chờ xác thực → Hệ thống gửi lại email (không giới hạn số lần).                                                                                                                   |
| AC-15 | Cá nhân NN — SĐT quốc tế*(UC255)*             | *(Scope: UC255 — không test tại UC252)* Chọn prefix quốc gia khác +84 → Nhập SĐT theo chuẩn E.164 (6–15 số) → Accepted. Nhập ít hơn 6 hoặc hơn 15 số → Inline error *"Số điện thoại không hợp lệ."* |
| AC-16 | Cá nhân NN — Mã định danh Hộ chiếu*(UC255)* | *(Scope: UC255 — không test tại UC252)* Nhập Hộ chiếu 6–9 ký tự Alphanumeric → Accepted. Nhập ký tự đặc biệt khác / vượt 9 ký tự / ít hơn 6 ký tự → Inline error *"Sai định dạng."*               |
| AC-17 | Cá nhân VN — Mã định danh CCCD                  | Nhập đúng 12 chữ số → Accepted. Nhập ít hơn 12 → Inline error *"Mã định danh nhập chưa đủ ký tự cho phép"*. Nhập nhiều hơn 12 → *"Mã định danh nhập quá ký tự cho phép"*.                                                                                                        |
| AC-18 | Error flow — mất mạng                              | Mất kết nối khi submit → Toast*"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + Nút Thử lại.                                                                                                          |
| AC-19 | Error flow — timeout                                 | API không phản hồi sau 10s → Toast*"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + Nút Thử lại.                                                                                                            |
| AC-20 | Error flow — lỗi 500                                | Server lỗi 5xx → Toast*"Hệ thống đang bận. Vui lòng thử lại sau."*                                                                                                                                                      |
| AC-21 | Validation Nơi cấp — để trống                    | Để trống Nơi cấp → focus out → Inline error *"Vui lòng nhập Nơi cấp"*                                                                                                                       |
| AC-22 | Validation Nơi cấp — quá dài                     | Nhập quá 500 ký tự vào Nơi cấp → focus out → Inline error *"Nơi cấp nhập quá ký tự cho phép"*.                                                                                                                             |
| AC-23 | Tổ chức/DN — Mã định danh                       | Nhập từ 1–12 chữ số → Accepted. Nhập quá 12 chữ số → Inline error *"Mã định danh nhập quá ký tự cho phép"*. Nhập ký tự không phải số → *"Mã định danh chỉ gồm các số 0-9."*                                                                     |
| AC-24 | Validation Họ và tên / Tên tổ chức — quá dài   | Nhập quá 50 ký tự → focus out → Inline error *"Họ và tên nhập quá ký tự cho phép"* (Cá nhân) hoặc *"Tên tổ chức nhập quá ký tự cho phép"* (Tổ chức) tùy loại tài khoản. |
| AC-25 | Validation Email — quá dài                       | Nhập quá 100 ký tự vào Email → focus out → Inline error *"Email nhập quá ký tự cho phép"*. |
| AC-26 | Validation SĐT — sai đầu số (+84)             | Nhập prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 (VD: 01xxx, 02xxx) → focus out → Inline error *"Số điện thoại không hợp lệ."* |

---

### 5. Lịch sử cập nhật

| Ngày      | Phiên bản  | Nội dung cập nhật                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 13/05/2026 | v1.0         | Khởi tạo tài liệu (Tách từ UC250-253_QuanLyTaiKhoan v3.4). Chuẩn hóa format.                                                                                                                                                                                                                                                                                                                                                                                                        |
| 14/05/2026 | v1.1         | Cập nhật theo feedback Q1-Q20: Bổ sung giấy tờ cho Cá nhân NN (Hộ chiếu), max length mật khẩu 50 ký tự, không chấp nhận special characters, bổ sung xử lý link hết hạn/invalid, xử lý gửi email thất bại, giữ nguyên form data & selected tile, loading spinner, reference CMR-07/CMR-16.                                                                                                                                                                       |
| 14/05/2026 | v1.2         | Q1: Link hết hạn → redirect về app + toast thay cho màn hình pending. Q2: SĐT Cá nhân NN → chuẩn E.164 (6–15 số). Q3: Nút Đăng ký → Disabled khi form lỗi HOẶC chưa check box (CMR-09). Q4: Lỗi trùng đồng thời → all inline errors. Q5: Bổ sung debounce CMR-18. Q6: Mật khẩu mặc định ẩn. Q7: Thêm Exclusions (social login ngoài scope). Q8: Bổ sung AC-06 đến AC-20. Q9: Phân biệt validation Hộ chiếu (6–9 alphanumeric) vs CCCD (12 số). |
| 14/05/2026 | v1.3         | IC-01: Cập nhật version header v1.0 → v1.3. IC-02: Bổ sung UI object nút "Gửi lại email" vào §2.3. IC-03: Đồng nhất arrow → Unicode. IC-05: Thêm error message Nơi cấp (min 2 ký tự, max 100 ký tự). IC-07: Link token không hợp lệ → redirect Đăng nhập + toast.                                                                                                                                                                                                |
| 14/05/2026 | v1.4         | IC-08: Đồng nhất tất cả arrow → Unicode toàn bộ §2.2 và §3.4. IC-09/10: Refactor §3.2 "Email gửi thất bại" — làm rõ flow sau đăng ký thành công, reference §2.3. IC-11: Sửa navigation nút Back §2.2 → về đúng Bước 1 (Chọn loại tài khoản). IC-12: Thêm AC-21/22 cho Nơi cấp validation (min 2, max 100 ký tự).                                                                                                                                  |
| 14/05/2026 | v1.5         | Bổ sung ghi chú mục §2.1 "Cá nhân nước ngoài": flow này được bàn giao sau cùng, thuộc phạm vi UC255.                                                                                                                                                                                                                                                                                                                                                                       |
| 14/05/2026 | v1.6         | Fix 4 inconsistencies: (1) Tiêu đề App Bar bổ sung variant Cá nhân NN; (2) MST validation tách rule rõ theo loại (Cá nhân VN: 10 số / Tổ chức: 10 hoặc 13 số); (3) Thêm note scope UC255 vào Mã định danh + SĐT Cá nhân NN tại §2.2 và AC-15/16; (4) Bổ sung AC-23 test Mã định danh Tổ chức/DN.                                                                                                                                                           |
| 14/05/2026 | v1.7         | Xóa bullet "Cá nhân nước ngoài (Hộ chiếu)" khỏi row Mã định danh §2.2 — nội dung thuộc scope UC255, không mô tả tại UC252.                                                                                                                                                                                                                                                                                                                                              |
| 14/05/2026 | v1.7 → v1.8 | Validation Max Length (3 trường) — Block input thay inline error |
| 17/05/2026 | v1.8 → v1.9 | CMR-09/CMR-03 — Chuẩn hoá required message: text field → "Vui lòng nhập [tên trường]", datepicker → "Vui lòng chọn [tên trường]", min length → "[tên trường] nhập chưa đủ ký tự cho phép". Password field giữ nguyên. |
| 19/05/2026 | v1.9 → v2.0 | CMR-09: Đổi block input → inline error: Tên/Họ tên (50ký tự), Nơi cấp (100 ký tự). Bổ sung Placeholder: Tên/Họ tên, Mã định danh, Nơi cấp, Mã số thuế, Email (CMR-09). Email format → *"Email không đúng định dạng"* (CMR-09). Date format → dd/MM/yyyy (CMR-12). Cập nhật AC-22. |
| 19/05/2026 | v2.0 → v2.1 | Đồng bộ rule validation với UC249/250: Email max length 100, SĐT (bỏ searchable, tách error length), Nơi cấp (max 500), chuẩn hoá thông báo lỗi Mã định danh & Mã số thuế ("chưa đủ ký tự cho phép"). |
| 19/05/2026 | v2.1 → v2.2 | Mã định danh Tổ chức/DN: sửa max từ 13 → 12 chữ số. Mã định danh & MST: chuẩn hoá error message sang "nhập chưa đủ/quá ký tự cho phép". Nơi cấp: bỏ rule min 2 ký tự, max 500. SĐT: bỏ searchable dropdown. Email: bổ sung max 100 ký tự + error message. |
| 19/05/2026 | v2.2 → v2.3 | Password: bỏ loại trừ khỏi auto-trim, áp dụng CMR-09 v1.7 (auto-trim cả password). SĐT prefix: ghi rõ không có ô tìm kiếm. Mã định danh: bổ sung error "Mã định danh chỉ gồm các số 0-9." khi nhập ký tự không phải số. Bổ sung AC-24 (Họ và tên max 50) và AC-25 (Email max 100). |
| 19/05/2026 | v2.3 → v2.4 | SĐT: bổ sung case validation prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ."*. Bổ sung AC-26. |
| 19/05/2026 | v2.4 → v2.5 | Mã định danh Tổ chức/DN: bỏ rule min 10 số, chỉ giữ max 12 chữ số. Cập nhật §2.2 và AC-23. |
