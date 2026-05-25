# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC256 — Đăng nhập ứng dụng Mobile
**Ngày tạo:** 29/04/2026
**Phiên bản:** v2.15
**Cập nhật:** 2026-05-24 — v2.15: Cập nhật luồng xử lý tự động gửi lại email khi đăng nhập tài khoản chưa xác thực.

| Thuộc tính              | Giá trị                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BA phụ trách            | huy.lai2                                                                                                                                                                                                 |
| Phân hệ                 | Ứng dụng Di động (Mobile App)                                                                                                                                                                        |
| Loại chức năng         | Xác thực & Phân quyền                                                                                                                                                                                |
| Đối tượng thực hiện | Cá nhân / Tổ chức                                                                                                                                                                                    |
| Ghi chú đối tượng    | Cá nhân: Mã định danh (CMND/CCCD) hoặc VNeID. Tổ chức: Mã số thuế (MST). VNeID không áp dụng cho Tổ chức. Trang chủ sau đăng nhập của Tổ chức có menu "Quản lý doanh nghiệp". |
| Giao diện                | Màn hình Mobile (Portrait)                                                                                                                                                                             |
| Ngày tạo                | 29/04/2026                                                                                                                                                                                               |
| Ngày cập nhật          | 24/05/2026                                                                                                                                                                                               |
| Phiên bản               | v2.14                                                                                                                                                                                                    |

---

## UC256 — Đăng nhập ứng dụng Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Đăng nhập ứng dụng Mobile
- **Mô tả:** Chức năng cho phép người dùng (cá nhân hoặc tổ chức) đăng nhập vào ứng dụng di động Cổng một cửa đầu tư Quốc gia bằng một trong các phương thức: nhập Mã định danh & Mật khẩu, hoặc đăng nhập qua VNeID.
- **Phân quyền:** Toàn bộ người dùng chưa đăng nhập (Guest).
- **Truy cập chức năng:** Mở ứng dụng di động → Màn hình đăng nhập hiển thị mặc định.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị cài đặt ứng dụng có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hệ thống khởi tạo phiên đăng nhập, lưu token an toàn và điều hướng người dùng tới Màn hình Trang chủ.
- **Chức năng đáp ứng usecase số:** UC256 (Phụ lục XIV — STT 256)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Chọn phương thức đăng nhập (Tham chiếu: Chọn cách đăng nhập (1).png)

**Mô tả giao diện:**
Màn hình khởi đầu. Nửa trên nền đỏ chứa logo và tiêu đề hệ thống. Nửa dưới nền trắng chứa các lựa chọn đăng nhập.

| #  | Tên trường                  | Kiểu trường | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                |
| -- | ------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Language Switcher              | Button (Icon)  | **Quy tắc hiển thị:**<br>- Nằm góc phải trên cùng. Gồm icon quả địa cầu và nhãn ngôn ngữ hiện tại (mặc định: "VI").<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Tap → Mở Bottom Sheet chọn ngôn ngữ (VI, EN, ZH, JA, KO). Chọn xong → Đóng Bottom Sheet, cập nhật nhãn ngôn ngữ.                 |
| 2  | Logo hệ thống                | Image          | **Quy tắc hiển thị:**<br>- Logo theo wireframe mới nhất.<br>- Văn bản dài (nếu có): **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Không tap được, không có action.                                                                                                                                                                          |
| 3  | Tên hệ thống                | Label          | **Quy tắc hiển thị:**<br>- Hiển thị: **"Cổng một cửa đầu tư Quốc gia"** (National Investment Gateway).<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Không tap được, không có action.                                                                                                                          |
| 4  | Tiêu đề chính              | Label          | **Quy tắc hiển thị:**<br>- Font to, đậm, màu trắng. Nội dung: **"Đăng nhập"**.<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Không tap được, không có action.                                                                                                                                                   |
| 5  | Phụ đề                      | Label          | **Quy tắc hiển thị:**<br>- Font nhỏ hơn tiêu đề, màu trắng. Nội dung: **"Chọn phương thức đăng nhập"**.<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Không tap được, không có action.                                                                                                                   |
| 6  | Card "Đăng nhập"            | Card           | **Quy tắc hiển thị:**<br>- Nền trắng, bo góc. Gồm icon user màu hồng, tiêu đề **"Đăng nhập"**, phụ đề **"Sử dụng mã định danh và mật khẩu"**.<br>- Văn bản dài trong card: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Tap → Chuyển sang màn hình Đăng nhập Mã định danh (§2.2).                      |
| 7  | Card "Đăng nhập với VNeID" | Card           | **Quy tắc hiển thị:**<br>- Nền trắng, bo góc. Gồm logo VNeID, tiêu đề **"Đăng nhập với VNeID"**, phụ đề về dịch vụ công.<br>- Văn bản dài trong card: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Tap → Mở app VNeID trên thiết bị (deep link). Nếu app VNeID chưa cài đặt → Điều hướng sang Store tải app. |
| 8  | Link "Đăng ký tài khoản"  | Link (Red)     | **Quy tắc hiển thị:**<br>- Màu đỏ. Nằm dưới divider "hoặc".<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Tap → Điều hướng sang UC252 (Đăng ký tài khoản).                                                                                                                                                         |
| 9  | Link "Quên mật khẩu"        | Link (Grey)    | **Quy tắc hiển thị:**<br>- Màu xám. Nằm cạnh link Đăng ký.<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Tap → Điều hướng sang UC253 (Quên mật khẩu).                                                                                                                                                                |
| 10 | Banner bảo mật               | Container      | **Quy tắc hiển thị:**<br>- Nằm dưới cùng, nền xám nhạt. Gồm icon bảo mật và text cam kết an toàn.<br>- Văn bản dài: **wrap xuống dòng** (không truncate).<br><br>**Quy tắc hành động:**<br>- Không tap được, không có action.                                                                                                                                 |

---

#### 2.2 Màn hình Đăng nhập Mã định danh (Tham chiếu: Đăng nhập bằng mã định danh, faceID.png)

**Mô tả giao diện:**
Form đăng nhập với 2 trường nhập liệu và các lựa chọn bổ sung. Nút "Đăng nhập" cố định ở dưới cùng màn hình (sticky bottom).

| # | Tên trường                      | Kiểu trường   | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Header                             | Component        | **Quy tắc hiển thị:**<br>- Nền đỏ. Gồm nút Back (←) bên trái và tiêu đề **"Đăng nhập Nhà đầu tư"** căn giữa.<br><br>**Quy tắc hành động:**<br>- Tap Back → Quay về màn hình Chọn phương thức đăng nhập (§2.1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 2 | Mã định danh                    | Textbox          | **Quy tắc hiển thị:**<br>- Label: **"Mã định danh*"** (có dấu * indicating bắt buộc).<br>- Placeholder: **"Nhập Mã định danh"**.<br>- Có icon thẻ (card) ở đầu trường nhập.<br>- Bàn phím: Numeric.<br>- Max length: **12 ký tự**.<br><br>**Quy tắc hành động:**<br>- Tap vào trường → Mở bàn phím numeric để nhập.<br>- Hệ thống auto-trim khoảng trắng đầu/cuối trước khi validate (CMR-09).<br><br>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường — tap sang trường khác hoặc tap ra ngoài)*:<br>- Để trống hoặc chỉ khoảng trắng → *"Vui lòng nhập Mã định danh"*<br>- Nhập sai độ dài (khác 12 chữ số — áp dụng cho cả Cá nhân VN và Tổ chức/DN vì Mã định danh luôn là CCCD/số định danh 12 số) → *"Mã định danh nhập chưa đủ 12 ký tự!"*<br>- Nhập ký tự không phải số (chữ cái, ký tự đặc biệt) → *"Mã định danh chỉ gồm các số 0-9"*<br>- Có dấu cách hoặc dấu gạch ngang → *"Mã định danh chỉ gồm các số 0-9"* |
| 3 | Mật khẩu                         | Password Input   | **Quy tắc hiển thị:**<br>- Label: **"Mật khẩu*"** (có dấu * indicating bắt buộc).<br>- Placeholder: **"Nhập mật khẩu"**.<br>- Có icon mắt (ẩn/hiện) bên phải trường nhập.<br>- Max length: **50 ký tự** (hiển thị lỗi on-blur, không chặn cứng).<br><br>**Quy tắc hành động:**<br>- Tap icon mắt → Toggle ẩn/hiện mật khẩu.<br>- Hệ thống auto-trim khoảng trắng đầu/cuối khi on blur (CMR-09).<br><br>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br>- Để trống → *"Vui lòng nhập Mật khẩu"*<br>- Vượt quá 50 ký tự → *"Mật khẩu không được vượt quá 50 ký tự!"*                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 4 | Link "Quên mật khẩu?"           | Link (Red)       | **Quy tắc hiển thị:**<br>- Màu đỏ. Nằm ngay dưới trường Mật khẩu.<br><br>**Quy tắc hành động:**<br>- Tap → Điều hướng sang UC253 (Quên mật khẩu).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 5 | Row Biometric                      | Row (Icon+Text)  | **Quy tắc hiển thị:**<br>- Gồm icon FaceID/Vân tay và text **"Đăng nhập bằng Face ID"** (hoặc **"Đăng nhập bằng Vân tay"** tùy thiết bị).<br>- **Chỉ hiện** khi đồng thời thỏa mãn **cả 2 điều kiện:**<br>  (a) User đã đăng nhập thành công bằng mật khẩu trên thiết bị này ít nhất một lần.<br>  (b) User đã **bật** cài đặt đăng nhập bằng Face ID/Vân tay trong UC254 (Cấu hình tài khoản → Cài đặt sinh trắc học).<br><br>**Quy tắc hành động:**<br>- Tap → Gọi OS Biometric Prompt. Chi tiết xem §3.2.                                                                                                                                                                                                                                                                                                                                                                 |
| 6 | Divider "Chưa có tài khoản?"   | Label            | **Quy tắc hiển thị:**<br>- Đường gạch ngang hai bên text "Chưa có tài khoản?" màu xám.<br><br>**Quy tắc hành động:**<br>- Không tap được.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 7 | Nút "Đăng ký tài khoản mới" | Button (Outline) | **Quy tắc hiển thị:**<br>- Viền xám, nền trắng. Luôn enabled.<br><br>**Quy tắc hành động:**<br>- Tap → Điều hướng sang UC252 (Đăng ký tài khoản).<br>- Có cơ chế debounce tránh double-tap (CMR-18).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 8 | Nút "Đăng nhập"                | Button (Primary) | **Quy tắc hiển thị:**<br>- Nền đỏ đậm, text trắng.<br>- **Sticky Bottom**: cố định dưới cùng màn hình, không cuộn theo nội dung.<br>- **Luôn Enabled** (nền đỏ). Không có trạng thái Disabled (CMR-09).<br><br>**Quy tắc hành động:**<br>- Tap → Validate toàn bộ form → Nếu hợp lệ: Hiển thị loading overlay → Gọi API đăng nhập. Nếu không hợp lệ: Hiển thị inline error dưới field lỗi.<br>- Có debounce tránh double-tap (CMR-18).                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Đăng nhập Mã định danh

**Main Flow:**

1. Người dùng nhập Mã định danh và Mật khẩu. Validation hiển thị **on-blur** (ngay khi rời khỏi trường — CMR-09):
   - Mã định danh trống / chỉ khoảng trắng → Inline error: *"Vui lòng nhập Mã định danh"*
   - Mã định danh sai độ dài (khác 12 chữ số — áp dụng cho cả Cá nhân và Tổ chức) → Inline error: *"Mã định danh nhập chưa đủ 12 ký tự!"*
   - Mã định danh chứa ký tự không phải số (chữ cái, ký tự đặc biệt, dấu cách, dấu gạch ngang) → Inline error: *"Mã định danh chỉ gồm các số 0-9"*
   - Mật khẩu trống → Inline error: *"Vui lòng nhập Mật khẩu"*
   - Mật khẩu vượt quá 50 ký tự → Inline error: *"Mật khẩu không được vượt quá 50 ký tự!"*
2. Nút "Đăng nhập" luôn Enabled (CMR-09). Tap → validate toàn bộ form → nếu có lỗi hiển thị inline error.
3. Tap nút "Đăng nhập" (khi Enabled, có debounce — CMR-18) → Hiển thị loading overlay.
4. Gọi API đăng nhập:
   - **Thành công (200):** Lưu token → Điều hướng sang Trang chủ.
   - **Sai thông tin (401):** Toast: *"Mã định danh hoặc mật khẩu không đúng. Vui lòng thử lại"*
   - **Lỗi 5xx:** Toast: *"Hệ thống đang bận. Vui lòng thử lại sau"* (CMR-07)

**Khóa tài khoản (Account Lockout):**

- **Đếm sai:** Nhập sai Mã định danh hoặc Mật khẩu **5 lần liên tiếp** → Khóa tài khoản 15 phút.
- **Phạm vi đếm:** Chỉ đếm sai Mã ĐD/MK, **không tính** sinh trắc học fail.
- **Ảnh hưởng VNeID:** VNeID **không bị ảnh hưởng** bởi counter khóa (VNeID dùng xác thực riêng).
- **UI feedback:** Chỉ hiển thị thông báo khóa khi đã bị khóa (không cảnh báo trước khi chưa khóa).
- **Toast thông báo:** *"Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút"*
- **Counter reset:** Sau 15 phút, tài khoản tự động mở khóa và counter đếm sai **reset về 0**.

**Error Flows:**

- **Timeout (>10s):** Toast: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại"* + Nút "Thử lại". (CMR-07, CMR-16)
- **Mất mạng:** Toast: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại"* + Nút "Thử lại". (CMR-07)
- **Tài khoản chưa xác thực email:** Hệ thống tự động gửi lại email xác thực mới. Toast: *"Tài khoản đã được đăng ký nhưng chưa xác thực. Hệ thống đã gửi lại email xác thực mới. Vui lòng kiểm tra email [email]"* (trong đó [email] là email đã đăng ký của tài khoản).

---

#### 3.2 Xử lý Sinh trắc học (Biometric)

**Điều kiện hiển thị:**

Row Biometric chỉ xuất hiện tại màn hình đăng nhập khi đồng thời thỏa mãn **cả 2 điều kiện**:

- **(a)** User đã đăng nhập thành công bằng mật khẩu trên thiết bị này ít nhất một lần.
- **(b)** User đã **bật** cài đặt đăng nhập bằng Face ID/Vân tay trong UC254 (Cấu hình tài khoản → Cài đặt sinh trắc học).

**Main Flow:**

1. User tap Row Biometric.
2. Hệ thống gọi Biometric Prompt của OS (FaceID/Vân tay).
3. OS nhận diện thành công → App nhận callback → Tự động login.

**Exception Flows:**

- **(a) Không nhận diện được (sai mặt/vân tay):**

  - Sau khi OS Biometric Prompt tự đóng và trả về callback lỗi, App bắt callback và hiển thị toast: *"Không nhận diện được, vui lòng thử lại"*
  - App không override UI của OS trong quá trình OS đang xử lý (đặc biệt trên iOS — Apple kiểm soát toàn bộ luồng FaceID prompt).
- **(b) User cancel OS prompt:**

  - OS đóng prompt.
  - App quay về form login, focus vào trường **Mã định danh** (ready for manual input).
- **(c) Sinh trắc bị OS khóa (quá 5 lần fail):**

  - Hiển thị popup: *"Sinh trắc học đã bị khóa do đã nhận diện sai 5 lần. Vui lòng đăng nhập bằng mật khẩu hoặc thử lại sau 15 phút"*
  - **Disable** Row Biometric (vẫn hiển thị nhưng không thể tương tác) cho đến khi user đăng nhập thành công bằng mật khẩu.
  - Reset: Vào Settings OS → Bảo mật → Sinh trắc học để bật lại, sau đó đăng nhập lại bằng mật khẩu để Row Biometric trở về trạng thái Enabled.

---

#### 3.3 Xử lý VNeID (Mở app trực tiếp)

**Main Flow:**

1. Người dùng tap Card "Đăng nhập với VNeID" tại màn hình §2.1.
2. Hệ thống kiểm tra:
   - **App VNeID đã cài đặt:** Mở app VNeID qua deep link/URL scheme.
   - **App VNeID chưa cài đặt:** Điều hướng sang Store (App Store / CH Play) để tải app.
3. Người dùng thực hiện đăng nhập trong app VNeID.
4. VNeID xác thực thành công → Gửi callback token về app MBFS.
5. App nhận token → Ánh xạ tài khoản → Điều hướng sang Trang chủ.

**Auto-create Account (Khi số định danh chưa có tài khoản):**

- **(a) Redirect về Đăng ký:** Sau khi VNeID xác thực thành công, nếu số định danh chưa có tài khoản trên hệ thống → App redirect về màn hình **Đăng ký tài khoản (UC252)**, tự động điền **Mã định danh** vào trường tương ứng. User hoàn tất đăng ký theo luồng UC252.
- **(b) Xử lý trùng:** Nếu số định danh đã liên kết tài khoản khác (đã đăng ký manual trước đó) → Hiển thị lỗi: *"Số định danh này đã được đăng ký. Vui lòng liên hệ hỗ trợ để được giải quyết"*

**Exception Flow — User bỏ dở VNeID:**

- **(c) User bỏ dở (force-close VNeID, nhấn Back về MBFS mà không hoàn thành xác thực):**
  - App MBFS quay về màn hình Chọn phương thức đăng nhập (§2.1) ở trạng thái bình thường.
  - Không hiển thị loading, không có timeout.
  - User có thể tap lại Card VNeID hoặc chọn phương thức đăng nhập khác.

---

#### 3.4 Đa ngôn ngữ (→ Xem CMR-17)

- **Ngôn ngữ mặc định:** Theo cài đặt thiết bị (→ CMR-17).
- **Đổi ngôn ngữ:** Tại màn hình §2.1, tap Language Switcher → Bottom Sheet chọn ngôn ngữ (VI, EN, ZH, JA, KO). Cập nhật tức thì toàn bộ nhãn, placeholder, thông báo lỗi.
- **Đồng bộ sau đăng nhập:** Sau khi đăng nhập thành công, hệ thống apply **ngôn ngữ từ server** (đã lưu từ thiết bị/web khác) và **ghi đè local**. Đảm bảo trải nghiệm nhất quán across devices.
- **Xung đột ngôn ngữ local vs server:** User chọn EN trên màn login → Đăng nhập vào tài khoản đã lưu VI trên server → Hệ thống tự động chuyển sang VI (override). **Không hiển thị thông báo chuyển ngôn ngữ.**

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

#### AC-01: Màn hình Chọn phương thức đăng nhập (§2.1)

| #       | Tiêu chí                                      | Pass condition                                                                    |
| ------- | ----------------------------------------------- | --------------------------------------------------------------------------------- |
| AC-01-1 | Language Switcher hoạt động                  | Tap → Mở Bottom Sheet chọn 5 ngôn ngữ. Chọn → Cập nhật nhãn ngôn ngữ. |
| AC-01-2 | Card "Đăng nhập" navigation                  | Tap → Chuyển sang màn hình Đăng nhập Mã định danh (§2.2).              |
| AC-01-3 | Card "Đăng nhập với VNeID" - có app        | Tap → Mở app VNeID trên thiết bị.                                            |
| AC-01-4 | Card "Đăng nhập với VNeID" - chưa cài app | Tap → Điều hướng sang Store tải app.                                        |
| AC-01-5 | Link "Đăng ký tài khoản"                   | Tap → Điều hướng sang UC252.                                                 |
| AC-01-6 | Link "Quên mật khẩu"                         | Tap → Điều hướng sang UC253.                                                 |

#### AC-02: Màn hình Đăng nhập Mã định danh (§2.2)

| #        | Tiêu chí                                           | Pass condition                                                                       |
| -------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------ |
| AC-02-1  | Validation Mã định danh - trống                  | Để trống →*"Vui lòng nhập Mã định danh"*                                  |
| AC-02-2  | Validation Mã định danh - sai độ dài            | Nhập sai độ dài (khác 12 chữ số — cả Cá nhân và Tổ chức) → Inline error *"Mã định danh nhập chưa đủ 12 ký tự!"*           |
| AC-02-4  | Validation Mã định danh - ký tự không hợp lệ | Nhập chữ cái →*"Mã định danh chỉ gồm các số 0-9"*                      |
| AC-02-5  | Validation Mật khẩu - trống                       | Để trống →*"Vui lòng nhập Mật khẩu"*                                       |
| AC-02-6  | Toggle ẩn/hiện mật khẩu                          | Tap icon mắt → Mật khẩu ẩn/hiện tương ứng.                                  |
| AC-02-7  | Row Biometric hiển thị đúng điều kiện         | Chỉ hiện khi thỏa mãn **cả 2 điều kiện**: (a) đã login thành công bằng mật khẩu ≥1 lần VÀ (b) đã bật cài đặt sinh trắc trong UC254. |
| AC-02-8  | Biometric login thành công                         | Tap Row Biometric → OS Prompt → Nhận diện thành công → Tự động login.      |
| AC-02-9  | Biometric fail - app handle (sau OS callback)    | Sai mặt/vân tay → OS prompt tự đóng → App nhận callback lỗi → Toast: *"Không nhận diện được, vui lòng thử lại"* |
| AC-02-10 | Biometric cancel                                     | Cancel OS Prompt → Quay về form, focus vào Mã định danh.                       |
| AC-02-11 | Biometric bị khóa OS                               | 5 lần fail → Popup thông báo + Row Biometric chuyển sang trạng thái **Disabled** (vẫn hiển thị, không tương tác được). |
| AC-02-12 | Login thành công                                   | API 200 → Lưu token → Điều hướng Trang chủ.                                  |
| AC-02-13 | Login thất bại (401)                               | Toast:*"Mã định danh hoặc mật khẩu không đúng. Vui lòng thử lại"*     |
| AC-02-14 | Khóa tài khoản                                    | 5 lần sai → Toast: *"Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút"* |
| AC-02-15 | Sticky bottom button                                 | Nút "Đăng nhập" cố định dưới cùng, không cuộn theo nội dung.            |
| AC-02-16 | Debounce                                             | Double-tap "Đăng nhập" không trigger 2 lần (CMR-18).                            |
| AC-02-17 | CMR-09: Trạng thái Nút Đăng nhập | Nút Đăng nhập luôn Enabled. Không có trạng thái Disabled. Tap → validate toàn bộ form → nếu có lỗi hiển thị inline error. |
| AC-02-19 | Validation Mật khẩu - vượt quá max length         | Nhập vượt quá 50 ký tự → Inline error *"Mật khẩu không được vượt quá 50 ký tự!"* |
| AC-02-20 | VNeID bỏ dở — quay về §2.1                       | User force-close VNeID hoặc nhấn Back → App quay về màn Chọn phương thức, không có loading/timeout. |
| AC-02-21 | VNeID bỏ dở — có thể chọn lại                   | Sau khi bỏ dở, User tap lại Card VNeID hoặc Card Đăng nhập → Hoạt động bình thường. |
| AC-02-22 | Language override sau login — không thông báo  | User chọn EN trên màn login → Đăng nhập vào tài khoản đã lưu VI → UI chuyển sang VI, không có thông báo. |
| AC-02-23 | VNeID Auto-create — redirect về UC252            | Số định danh từ VNeID chưa có tài khoản → App redirect về màn hình Đăng ký tài khoản (UC252), trường Mã định danh được tự động điền. |
| AC-02-24 | Biometric Disabled — Reset via password login     | Sau khi Row Biometric bị Disable (khóa OS) → User đăng nhập thành công bằng mật khẩu → Row Biometric trở về Enabled. |
| AC-02-25 | Lockout counter reset về 0                        | Tài khoản bị khóa 15 phút → Sau 15 phút tự mở khóa → Counter đếm sai reset về 0 (lần sai tiếp theo bắt đầu đếm lại từ 1). |
| AC-02-26 | Login thất bại — TK chưa xác thực email       | Đăng nhập bằng TK đã đăng ký nhưng chưa xác thực email → Tự động gửi lại email xác thực mới. Toast: *"Tài khoản đã được đăng ký nhưng chưa xác thực. Hệ thống đã gửi lại email xác thực mới. Vui lòng kiểm tra email [email]"* (với [email] là email đã đăng ký của tài khoản). |

---

### 5. Yêu cầu phi chức năng (NFR)

#### NFR-SEC: Bảo mật màn hình đăng nhập

| # | Hạng mục | Quyết định | Ghi chú |
| - | --------- | ----------- | -------- |
| NFR-SEC-01 | Jailbreak/Root detection | **Không chặn** đăng nhập trên thiết bị bị root/jailbreak. | Không yêu cầu trong phiên bản này. |
| NFR-SEC-02 | Screenshot prevention | **Không block** screenshot trên màn hình có mật khẩu. | Không yêu cầu trong phiên bản này. |
| NFR-SEC-03 | Certificate Pinning | App **không** kiểm tra SSL certificate pinning khi gọi API đăng nhập. | Không yêu cầu trong phiên bản này. |

---

### 6. Lịch sử cập nhật

| Ngày      | Phiên bản  | Mục cập nhật                                                      | Before                                                       | After                                                                                                      | Ghi chú                       |
| ---------- | ------------ | -------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 2026-05-11 | v1 → v1.1   | Đa ngôn ngữ                                                       | (Không có)                                                 | Bổ sung section đa ngôn ngữ                                                                            | CMR-17                         |
| 2026-05-12 | v1.1 → v1.2 | Timeout                                                              | 30s                                                          | 10s                                                                                                        | CMR-16                         |
| 2026-05-12 | v1.2 → v1.3 | Cập nhật UI & Logic                                                | Form cũ, không có biometric logic, thiếu chi tiết VNeID | Cập nhật tên hệ thống, Language Switcher, Biometric logic, VNeID WebView, sticky bottom               | Theo Feedback BA & Wireframe   |
| 2026-05-12 | v1.3 → v1.4 | Bổ sung validation, exception flow, khóa 5 lần, VNeID auto-create | (Không có)                                                 | (a) Mã ĐD: 12 số, (b) Biometric 3 scenario, (c) Khóa 5 lần scope, (d) VNeID auto-create               | Q1, Q2, Q5, Q10, Q11, Q13      |
| 2026-05-13 | v1.4 → v1.5 | Biometric exception                                                  | OS handle retry                                              | App trực tiếp bắt lỗi, hiển thị toast                                                                | Cập nhật theo yêu cầu      |
| 2026-05-13 | v1.5 → v1.6 | Validation Mã định danh                                           | 6-12 alphanumeric                                            | 12 số (CCCD)                                                                                              | Đồng bộ với VNeID          |
| 2026-05-13 | v1.6 → v2.0 | Cập nhật format chi tiết                                          | Mô tả chung, thiếu Quy tắc hiển thị/hành động       | Bổ sung Quy tắc hiển thị, Quy tắc hành động, Validation cho từng trường. Bổ sung AC chi tiết. | Áp dụng format UC249         |
| 2026-05-13 | v2.0 → v2.1 | VNeID flow                                                           | WebView embed                                                | Mở app VNeID trực tiếp (deep link). Nếu chưa cài → điều hướng sang Store.                       | Cập nhật theo wireframe mới |
| 2026-05-13 | v2.1 → v2.2 | Mật khẩu: xóa auto-trim, thêm max 50 ký tự; Khóa TK: tooltip → toast | auto-trim password (CMR-09), Tooltip, Không có max length | Không trim password (CMR-09 loại trừ), Max 50 ký tự, Toast khi bị khóa TK, AC-02-14 cập nhật | Audit v1 — Q1, Q2, Q3 |
| 2026-05-13 | v2.2 → v2.3 | Bổ sung điều kiện (b) biometric §3.2; Follow CMR-09 disable Submit button; Sửa Ẩn→Disable Row Biometric khi khóa OS; Làm rõ iOS toast after callback; Bổ sung VNeID bỏ dở exception; Sub-cases ngôn ngữ (a)(b); Cập nhật AC-02-7/9/11; Bổ sung AC-02-17 đến AC-02-25; Bổ sung NFR-SEC section | Nhiều mục | Xem chi tiết từng section | Audit v3 — feedback round 2 |
| 2026-05-13 | v2.3 → v2.4 | Fix §2.2 Item 8 (xóa "Luôn enabled", áp CMR-09 Disabled/Enabled); Bổ sung counter reset về 0 sau lockout; Cập nhật VNeID Auto-create (redirect UC252 thay Bottom Sheet); Xóa Sub-case (a) ngôn ngữ (→ CMR-17); Cập nhật AC-02-23/24, bổ sung AC-02-26; Đảo §5/§6 numbering | Nhiều mục | Xem chi tiết từng section | Audit v3 — G-01 đến G-05 |
| 2026-05-17 | v2.4 → v2.5 | CMR-09/CMR-03 — Chuẩn hoá required message | `"Mã định danh là bắt buộc."` | `"Vui lòng nhập Mã định danh"` | Đồng bộ CMR-09 v1.7 |
| 2026-05-17 | v2.5 → v2.6 | CMR-09 — Chuẩn hoá required message Password | `"Mật khẩu là bắt buộc."` | `"Vui lòng nhập Mật khẩu!"` | Đồng bộ CMR-09 v1.7 — áp dụng đồng nhất cả password field |
| 2026-05-18 | v2.6 → v2.7 | Bổ sung Error Flow: TK chưa xác thực email | (Không có) | Thêm case đăng nhập bằng TK chưa xác thực email → Toast: "Tài khoản đang chờ xác thực email."; Bổ sung AC-02-26 | Theo Feedback BA |
| 2026-05-21 | v2.7 → v2.8 | Align CMR Mobile v6.0 | 1. Nút "Đăng nhập" Disabled→Luôn Enabled. 2. Bỏ dấu "." cuối inline validation errors. 3. Thêm rule CMR-11 cho Mã định danh. |
| 2026-05-21 | v2.8 → v2.9 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v2.9 → v2.10 | Align CMR Rule H — Bỏ dấu `.` cuối toast/popup/error | 9 message có dấu `.` cuối câu | Bỏ dấu `.` cuối tất cả toast, popup, error message (401, 5xx, lockout, timeout, mất mạng, chưa xác thực, biometric fail/khóa, VNeID trùng) | Theo CMR Rule H — BA confirmed áp dụng cho tất cả message |
| 2026-05-21 | v2.10 → v2.11 | Align CMR-09 v1.9 — Password trim + Placeholder | (B) "Không auto-trim password"; (C) Placeholder "Nhập mã định danh của bạn" | (B) Password cũng áp dụng auto-trim khi on blur (CMR-09 v1.7+); (C) Placeholder → "Nhập mã định danh" (chuẩn CMR-09) | Đồng bộ CMR_Mobile v1.9 |
| 2026-05-22 | v2.11 → v2.12 | Cập nhật rule độ dài Mã định danh | Cá nhân: 12 số; Tổ chức: 10 số | Mã định danh luôn 12 số (cả Cá nhân và Tổ chức — vì là CCCD/số định danh cá nhân người đại diện) | Đồng bộ với UC252 v2.13 |
| 2026-05-22 | v2.12 → v2.13 | Thống nhất error message Mật khẩu | `"Vui lòng nhập Mật khẩu"` (không !) trong lịch sử v2.6 | `"Vui lòng nhập Mật khẩu!"` (có !) — đồng nhất với UC252 | Sửa conflict giữa UC256 và UC252 |
| 2026-05-24 | v2.13 → v2.14 | Bổ sung validation Mật khẩu > 50 ký tự | AC-02-19: Cap cứng ở 50 ký tự | Chuyển sang soft limit, hiển thị inline error "Mật khẩu không được vượt quá 50 ký tự!" | Cập nhật theo yêu cầu |
| 2026-05-24 | v2.14 → v2.15 | Đăng nhập bằng tài khoản chưa xác thực | Toast *"Tài khoản đang chờ xác thực email"* | Tự động gửi lại email xác thực mới. Đổi toast thành *"Tài khoản đã được đăng ký nhưng chưa xác thực..."* đồng bộ UC252 | Cập nhật theo yêu cầu |
