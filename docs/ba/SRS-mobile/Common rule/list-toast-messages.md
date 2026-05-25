# BẢNG THÔNG BÁO LỖI & THÔNG BÁO HỆ THỐNG
## Phân hệ Mobile App | Hệ thống MBFS

> Tài liệu này tổng hợp toàn bộ các thông báo (Toast, Popup) được sử dụng trong ứng dụng Mobile MBFS.
> Đây là nguồn tham chiếu duy nhất cho QC và Dev khi triển khai thông báo hệ thống.

---

## 1. Toast Messages

Toast hiển thị overlay trên toàn màn hình, tự động biến mất sau **3 giây** (chuẩn hóa theo UC257 — áp dụng thống nhất toàn ứng dụng).

### 1.1 Nhóm Xác thực & Phiên đăng nhập

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T01** | Phiên đăng nhập hết hạn (HTTP 401, refresh token > 15 ngày) | Phiên đăng nhập hết hạn | 🔴 Error | CMR-07, toàn bộ UC yêu cầu login |
| **T02** | Đăng nhập thất bại — sai Mã định danh hoặc mật khẩu (HTTP 401) | Mã định danh hoặc mật khẩu không đúng. Vui lòng thử lại | 🔴 Error | UC256 |
| **T03** | Đăng nhập thất bại — tài khoản bị tạm khóa (nhập sai ≥ 5 lần) | Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút | 🔴 Error | UC256 |
| **T04** | Đăng nhập thất bại — tài khoản chưa xác thực email | Tài khoản đang chờ xác thực email | 🔴 Error | UC256 |
| **T05** | Sinh trắc học (FaceID/Vân tay) nhận diện thất bại (OS callback lỗi) | Không nhận diện được, vui lòng thử lại | 🔴 Error | UC256 |
| **T06** | VNeID — số định danh đã liên kết tài khoản khác | Số định danh này đã được đăng ký. Vui lòng liên hệ hỗ trợ để được giải quyết | 🔴 Error | UC256 |
| **T07** | Truy cập chức năng yêu cầu đăng nhập khi chưa đăng nhập | Vui lòng đăng nhập để xem hồ sơ đầu tư | 🔴 Error | UC92 |

### 1.2 Nhóm Đăng ký & Quản lý tài khoản

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T08** | Đăng ký / Cập nhật TK — trùng Email | Email đã tồn tại | 🔴 Error | UC252, UC249 |
| **T09** | Đăng ký / Cập nhật TK — trùng Số điện thoại | Số điện thoại đã tồn tại | 🔴 Error | UC252, UC249 |
| **T10** | Đăng ký tài khoản — trùng Mã định danh | Mã định danh đã tồn tại | 🔴 Error | UC252 |
| **T11** | Đăng ký tài khoản — trùng Mã số thuế | Mã số thuế đã tồn tại | 🔴 Error | UC252 |
| **T12** | Đăng ký lại với MĐD/MST chưa xác thực (ghi đè record cũ, gửi lại email) | Tài khoản đã được đăng ký nhưng chưa xác thực. Hệ thống đã gửi lại email xác thực mới. Vui lòng kiểm tra email [email] | 🔴 Error | UC252 |
| **T13** | Quên mật khẩu — nhập MĐD không tồn tại trong DB | Mã định danh không tồn tại trên hệ thống | 🔴 Error | UC253, UC252 |
| **T14** | Quên mật khẩu — nhập MĐD của TK chưa xác thực | Tài khoản chưa được xác thực. Vui lòng thực hiện Đăng ký lại để nhận email xác thực mới | 🔴 Error | UC253, UC252 |
| **T15** | Link xác thực email hết hạn (> 1 ngày) | Link xác thực đã hết hạn, vui lòng thử lại | 🔴 Error | UC252 |
| **T16** | Link xác thực email token không hợp lệ | Nội dung không tồn tại hoặc đã bị xóa | 🔴 Error | UC252 |
| **T17** | Gửi email xác thực thất bại (SMTP error, inbox full, spam filter) | Không thể gửi email xác thực. Vui lòng thử lại | 🔴 Error | UC252 |
| **T18** | Link đặt lại mật khẩu hết hạn (> 1 ngày) | Link đặt lại mật khẩu đã hết hạn. Vui lòng thử lại | 🔴 Error | UC253 |
| **T19** | Cập nhật thông tin tài khoản cá nhân thành công | Cập nhật thông tin tài khoản thành công! | 🟢 Success | UC249 |

### 1.3 Nhóm Đổi mật khẩu & Đăng xuất

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T20** | Đổi mật khẩu thành công (luồng UC251 — từ màn hình Đổi MK độc lập) | Đổi mật khẩu thành công | 🟢 Success | UC251 |
| **T21** | Đổi mật khẩu thành công (luồng UC257 — từ màn hình Cài đặt) | Đổi mật khẩu thành công. Vui lòng đăng nhập lại | 🟢 Success | UC257 |
| **T22** | Đổi MK UC251 — tài khoản bị khóa tạm thời (nhập sai MK cũ ≥ 5 lần) | Tài khoản của bạn đã bị khóa tạm thời. Vui lòng thử lại sau 15 phút | 🔴 Error | UC251 |
| **T23** | Đăng xuất thành công (bao gồm cả fallback: timeout / mất mạng / lỗi API) | Đăng xuất thành công | 🟢 Success | UC257 |

### 1.4 Nhóm Cài đặt tài khoản (Toggle thông báo)

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T24** | Tắt toggle "Nhận thông báo hệ thống" (UC258) | Bạn sẽ không nhận được thông báo hệ thống nữa | 🔴 Error | UC254/UC258 |
| **T25** | Tắt toggle "Nhận thông báo kết quả xử lý hồ sơ" (UC259) | Bạn sẽ không nhận được thông báo kết quả xử lý hồ sơ nữa | 🔴 Error | UC254/UC259 |

> **Lưu ý T24, T25:** Bật toggle → **Không hiển thị toast**.

### 1.5 Nhóm Tải file & Tương tác nội dung

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T26** | Tải văn bản pháp luật thành công | Tải văn bản thành công | 🟢 Success | UC69 |
| **T27** | Tải file kho dữ liệu điện tử thành công | Tải xuống thành công | 🟢 Success | UC52 |
| **T28** | Tải file kho dữ liệu điện tử thất bại | Tải xuống thất bại. Vui lòng thử lại | 🔴 Error | UC52 |
| **T29** | Tải tệp báo cáo đã nộp thành công | Tải tệp thành công | 🟢 Success | UC54 |
| **T30** | Tải tệp báo cáo đã nộp thất bại | Tải tệp thất bại. Vui lòng thử lại | 🔴 Error | UC54 |
| **T31** | File đính kèm không còn tồn tại trên server (UC69, UC70) | Nội dung không tồn tại hoặc đã bị xóa | 🔴 Error | UC69, UC70 |
| **T32** | Sao chép mã thủ tục vào clipboard (UC70) | Đã sao chép | 🟢 Success | UC70 |

### 1.6 Nhóm Đăng ký quan tâm dự án (UC87)

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T33** | Đăng ký quan tâm dự án thành công | Đăng ký quan tâm thành công | 🟢 Success | UC87 |
| **T34** | Hủy đăng ký quan tâm dự án thành công | Đã hủy đăng ký quan tâm | 🟢 Success | UC87 |
| **T35** | Đăng ký quan tâm dự án thất bại | Đăng ký quan tâm thất bại. Vui lòng thử lại | 🔴 Error | UC87 |
| **T36** | Hủy đăng ký quan tâm dự án thất bại | Hủy quan tâm thất bại. Vui lòng thử lại | 🔴 Error | UC87 |
| **T37** | Lưu thông tin nhà đầu tư (Form đăng ký quan tâm) thất bại | Lưu thông tin thất bại. Vui lòng thử lại | 🔴 Error | UC87 |

### 1.7 Nhóm Chatbot (UC60-61)

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu UC |
| :--- | :--- | :--- | :--- | :--- |
| **T38** | Lỗi lưu phiên chat (background save fail) | Không thể lưu phiên. Vui lòng thử lại | 🔴 Error | UC60-61 |

> **Lưu ý T38:** Hội thoại vẫn tiếp tục bình thường khi lỗi lưu phiên. Timeout Chatbot đặc biệt là **30 giây** (khác CMR-16 = 10s) vì API AI cần thời gian xử lý ngôn ngữ tự nhiên.

### 1.8 Nhóm Lỗi hệ thống & Kết nối (Toàn cục — CMR-07)

| Mã | Trường hợp | Nội dung thông báo | Loại | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- |
| **T39** | Lỗi API / Server (HTTP 5xx) | Hệ thống đang bận. Vui lòng thử lại sau | 🔴 Error | CMR-07, toàn bộ UC |
| **T40** | Mất kết nối mạng | Không thể kết nối. Vui lòng kiểm tra mạng và thử lại | 🔴 Error | CMR-07, toàn bộ UC |
| **T41** | Timeout API (> 10 giây) | Yêu cầu đã hết thời gian chờ. Vui lòng thử lại | 🔴 Error | CMR-07, CMR-16, toàn bộ UC |

---

## 2. Inline Validation Messages

Hiển thị ngay bên dưới trường nhập liệu, màu đỏ, khi on-blur hoặc khi Submit.

| Mã | Trường hợp | Nội dung thông báo | Vị trí hiển thị | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- |
| **V01** | Trường text bắt buộc bị bỏ trống | Vui lòng nhập [tên trường] | Bên dưới trường, màu đỏ | CMR-09 |
| **V02** | Trường dropdown bắt buộc chưa chọn | Vui lòng chọn [tên trường] | Bên dưới trường, màu đỏ | CMR-03 |
| **V03** | Trường vượt quá ký tự tối đa | [Tên trường] không được vượt quá [maxlength] ký tự! | Bên dưới trường, màu đỏ | CMR-09 |
| **V04** | Trường chưa đủ ký tự tối thiểu | [Tên trường] nhập chưa đủ [minlength] ký tự! | Bên dưới trường, màu đỏ | CMR-09 |
| **V05** | Trường Mã (Code Field) — chứa khoảng trắng hoặc ký tự có dấu | Mã không bao gồm khoảng trắng và ký tự có dấu | Bên dưới trường, màu đỏ | CMR-09 |
| **V06** | Mã định danh bỏ trống | Vui lòng nhập Mã định danh | Bên dưới trường, màu đỏ | UC256 |
| **V07** | Mã định danh có độ dài khác 10 và 12 chữ số | Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số! | Bên dưới trường, màu đỏ | UC256 v2.12 |
| **V08** | Mã định danh nhập ký tự không phải số (chữ cái, ký tự đặc biệt, dấu cách, gạch ngang) | Mã định danh chỉ gồm các số 0-9 | Bên dưới trường, màu đỏ | UC256 |
| **V09** | Mật khẩu bỏ trống | Vui lòng nhập Mật khẩu | Bên dưới trường, màu đỏ | UC256 |
| **V10** | Sai mật khẩu hiện tại khi đổi mật khẩu (< 5 lần, không kèm Toast) | Mật khẩu hiện tại không đúng | Bên dưới trường, màu đỏ | UC251 |
| **V11** | Searchable Dropdown — không có kết quả khớp với từ khóa nhập | Không có dữ liệu | Trong danh sách option, căn giữa | CMR-03 |

---

## 3. Popup (Alert không tự biến mất)

| Mã | Trường hợp | Nội dung thông báo | Nút đi kèm | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- |
| **P01** | Xác nhận trước khi đăng xuất | Bạn có chắc chắn muốn đăng xuất không? | [Xác nhận] / [Hủy] | UC257 |
| **P02** | Sinh trắc học bị OS khóa (nhận diện sai 5 lần) | Sinh trắc học đã bị khóa do đã nhận diện sai 5 lần. Vui lòng đăng nhập bằng mật khẩu hoặc thử lại sau 15 phút | [Đồng ý] | UC256 |

---

## 4. Empty State Messages (Trạng thái trống)

Hiển thị ở giữa vùng nội dung chính khi không có dữ liệu.

| Mã | Trường hợp | Nội dung thông báo | Tham chiếu |
| :--- | :--- | :--- | :--- |
| **ES01** | Danh sách trống — API trả về không có dữ liệu | Không có dữ liệu | CMR-14, toàn bộ UC |
| **ES02** | Tìm kiếm / lọc không có kết quả phù hợp | Không tìm thấy kết quả | CMR-14, CMR-01, toàn bộ UC |

---

## 5. Phân biệt Toast vs Inline Error vs Popup

| Tiêu chí | Toast | Inline Error | Popup |
| :--- | :--- | :--- | :--- |
| **Vị trí** | Overlay toàn màn hình | Ngay dưới trường nhập liệu | Dialog chặn tương tác |
| **Thời gian** | Tự biến mất sau 3 giây | Giữ nguyên cho đến khi trường hợp lệ | Không tự biến mất, cần user action |
| **Khi nào dùng** | Kết quả thao tác cấp màn hình (API success/fail) | Lỗi validation từng trường | Yêu cầu xác nhận hoặc thông báo nghiêm trọng |
| **Ví dụ** | T23 (đăng xuất thành công), T39 (lỗi 5xx) | V01 (trường bắt buộc), V07 (MĐD sai độ dài) | P01 (xác nhận đăng xuất), P02 (sinh trắc bị khóa) |

---

## 6. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-22 | 1.0 | Khởi tạo — tổng hợp từ toàn bộ UC Mobile | (Không có) | T01–T34, V01–V14, A01, P01, ES01–ES02 | Tạo mới — đồng bộ CMR_Mobile v1.10 |
| 2026-05-22 | 1.0 → 1.1 | Sửa mô tả vị trí Toast | "hoặc bottom sheet" | Overlay toàn màn hình | Sai kỹ thuật |
| 2026-05-22 | 1.1 → 1.2 | Chuẩn hóa loại Toast | Có 🟡 Warning | Chỉ 🟢 Success và 🔴 Error | Đồng nhất với chuẩn Report |
| 2026-05-22 | 1.2 → 1.3 | Full rescan toàn bộ SRS-mobile | T01–T34 | T01–T41 (bổ sung T24–T25 UC254/258/259, T32 copy clipboard UC70, T38 Chatbot lưu phiên, T18 link đặt lại MK, tách T26–T30 download UC52/54/69) | Phát hiện các toast bị thiếu từ UC52, UC54, UC60-61, UC70, UC253, UC254 |
| 2026-05-22 | 1.2 → 1.3 | Cập nhật V07 theo UC256 v2.12 | "< 10 số → Sai định dạng" và "> 13 số → nhập quá ký tự" | "khác 10/12 số → Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!" | UC256 v2.12 gộp rule |
| 2026-05-22 | 1.2 → 1.3 | Tách P02 ra khỏi Alert | Popup sinh trắc bị khóa nằm trong Alert | Chuyển sang mục Popup (P02) | Phân loại đúng hơn |
