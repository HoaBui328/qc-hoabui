# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC249 — Quản lý thông tin tài khoản cá nhân trên Mobile
**Ngày tạo:** 29/04/2026
**Phiên bản:** v2.23
**Cập nhật:** 21/05/2026 — Đồng bộ CMR Mobile 20260520 (Auto-trim, Dropdown search, Rule Mã bưu chính).

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Quản lý tài khoản |
| Đối tượng thực hiện | Cá nhân (đã đăng nhập) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 29/04/2026 |
| Phiên bản | v2.23 |

> **Phạm vi UC này:** Chỉ áp dụng cho tài khoản loại **Cá nhân**. Tài khoản **Tổ chức** được xử lý ở màn hình riêng (không thuộc UC249).

---

## UC249 — Quản lý thông tin tài khoản cá nhân trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Quản lý thông tin tài khoản cá nhân trên Mobile
- **Mô tả:** Chức năng cho phép người dùng xem toàn bộ thông tin tài khoản cá nhân (Hồ sơ + Thông tin định danh) và chỉnh sửa các trường được phép cập nhật. Bao gồm hai màn hình chính: Xem chi tiết (read-only) và Chỉnh sửa thông tin.
- **Phân quyền:** Cá nhân đã đăng nhập.
- **Phạm vi ngoài UC (Exclusions):** UC này KHÔNG bao gồm: quản lý thông tin tài khoản **Tổ chức-DN** (xử lý ở màn hình riêng — UC250), đổi mật khẩu (UC251), thay đổi loại tài khoản.
- **Truy cập chức năng:** Sidebar → **"Cấu hình tài khoản"** → Tap **"Thông tin cá nhân"**.
- **Điều kiện tiên quyết (Preconditions):** Người dùng đã đăng nhập vào ứng dụng (session còn hiệu lực). Loại tài khoản là **Cá nhân**.
- **Điều kiện kết thúc (Postconditions):** Thông tin tài khoản được lưu xuống DB với dữ liệu mới nhất. Session không bị ảnh hưởng (người dùng không bị đăng xuất). Màn hình Xem chi tiết tự động hiển thị dữ liệu đã cập nhật mới nhất.
- **Chức năng đáp ứng usecase số:** UC249 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Giao diện Xem chi tiết thông tin tài khoản cá nhân (UC249 — Read-only)

**Mô tả giao diện:**
Màn hình dạng danh sách thông tin (Detail View). App Bar tiêu đề **"Tài khoản cá nhân"** với nút Back (←) bên trái và nút Edit (✏️) bên phải. Nội dung chia thành 2 section: **Hồ sơ** và **Thông tin**. Hỗ trợ Pull-to-Refresh (CMR-13).

**App Bar:**

| # | Thành phần | Kiểu | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Nút Back (←) | Icon Button | **Quy tắc hiển thị:**<br/>- Luôn hiển thị ở góc trái header (CMR-06).<br/><br/>**Quy tắc hành động:**<br/>- Tap → Quay về màn hình Cấu hình tài khoản. |
| 2 | Tiêu đề | Label | **Quy tắc hiển thị:**<br/>- Hiển thị cố định: **"Tài khoản cá nhân"**. Căn giữa header. |
| 3 | Nút Edit (✏️) | Icon Button | **Quy tắc hiển thị:**<br/>- Luôn hiển thị với mọi tài khoản Cá nhân. Góc phải header.<br/><br/>**Quy tắc hành động:**<br/>- Tap → Chuyển sang màn hình Chỉnh sửa (UC249.1).<br/>- Có cơ chế debounce tránh double-tap (CMR-18). |

**Section "Hồ sơ":**

| # | Tên trường | Kiểu trường | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Họ và tên | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Hiển thị họ tên đầy đủ từ tài khoản.<br/>- Văn bản dài: **wrap xuống dòng** (không truncate) — ưu tiên hiển thị đầy đủ họ tên.<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 2 | Email | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Hiển thị địa chỉ email từ tài khoản.<br/>- Văn bản dài: hiển thị tối đa **1 dòng**, quá dài **truncate (…)** ở cuối.<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 3 | Số điện thoại | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Hiển thị số điện thoại kèm country code. VD: **+84 912 345 678**.<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 4 | Loại tài khoản | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Luôn hiển thị giá trị cố định: **"Cá nhân"**. Không bao giờ null.<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |

**Section "Thông tin":**

| # | Tên trường | Kiểu trường | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Mã định danh | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Hiển thị Mã CMND/CCCD từ hệ thống.<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 2 | Ngày cấp | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Định dạng: **DD/MM/YYYY** (CMR-12).<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 3 | Nơi cấp | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Hiển thị nơi cấp giấy tờ. Văn bản dài → **wrap xuống dòng** (không truncate).<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 4 | Mã số thuế | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 5 | Quốc gia | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 6 | Tỉnh/Thành phố | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 7 | Phường/Xã | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 8 | Địa chỉ | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Văn bản dài → **wrap xuống dòng** (không truncate).<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |
| 9 | Mã bưu chính | Label (Read-only) | **Quy tắc hiển thị:**<br/>- Nếu API trả null → hiển thị **"-"** (CMR-14).<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không có action. |

---

#### 2.2 Giao diện Chỉnh sửa thông tin tài khoản cá nhân (UC249.1)

**Mô tả giao diện:**
Form chỉnh sửa thông tin tài khoản cá nhân. Nội dung chia thành 2 section có thể thu gọn (Collapsible): **Hồ sơ** và **Thông tin**. Cuối trang có 2 nút hành động cố định (sticky bottom): **Lưu thay đổi** và **Hủy**. Tham chiếu: CMR-09.

> **Quy tắc hiển thị lỗi chung (áp dụng cho tất cả trường nhập liệu):** Lỗi validation hiển thị **ngay khi người dùng rời khỏi trường** (focus out / chuyển sang trường khác / tap ra ngoài). Không chờ đến khi nhấn "Lưu thay đổi". Thông báo lỗi hiển thị inline màu đỏ, ngay dưới trường tương ứng (CMR-09).

**App Bar:**

| # | Thành phần | Kiểu | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Nút Back (←) | Icon Button | **Quy tắc hiển thị:**<br/>- Luôn hiển thị ở góc trái header (CMR-06).<br/><br/>**Quy tắc hành động:**<br/>- Tap → Quay về Xem chi tiết.<br/>- Nhấn **Android Back button vật lý** khi đang ở màn này: áp dụng cùng logic như nút Back (←) ở trên. |
| 2 | Tiêu đề | Label | **Quy tắc hiển thị:**<br/>- Hiển thị cố định: **"Tài khoản cá nhân"**. Căn giữa header. |

**Section "Hồ sơ" (Collapsible — mặc định mở):**

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Họ và tên | Label (Read-only) | — | **Quy tắc hiển thị:**<br/>- Nền xám, viền disabled. Giá trị load từ dữ liệu tài khoản hiện tại.<br/>- Không bao giờ null trên form chỉnh sửa.<br/><br/>**Quy tắc hành động:**<br/>- Không chỉnh sửa được. Tap vào trường → Không mở bàn phím. |
| 2 | Email | Textbox (email) | ✱ | **Quy tắc hiển thị:**<br/>- Đánh dấu (*) bên cạnh label.<br/>- Giá trị mặc định: load từ dữ liệu tài khoản hiện tại.<br/>- **Max length: 100 ký tự** (CMR-11).<br/>- Placeholder: *"Nhập Email"*.<br/><br/>**Quy tắc hành động:**<br/>- Người dùng chỉnh sửa địa chỉ email. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập địa chỉ email"*<br/>- Nhập quá 100 ký tự → *"Email không được vượt quá 100 ký tự!"* (CMR-09)<br/>- Không có ký tự @ → *"Email không đúng định dạng"*<br/>- Không có phần domain (VD: abc@) → *"Email không đúng định dạng"*<br/>- Không có phần extension (VD: abc@domain) → *"Email không đúng định dạng"*<br/>- Có khoảng trắng giữa chuỗi (VD: abc @gmail.com) → *"Email không đúng định dạng"* |
| 3 | Số điện thoại | Textbox (tel) + Country Code Prefix | ✱ | **Quy tắc hiển thị:**<br/>- Đánh dấu (*) bên cạnh label.<br/>- Ô nhập gồm 2 phần: **[Cờ quốc gia + Mã vùng]** (prefix, bên trái) và **[Ô nhập số]** (bên phải).<br/>- Mặc định: 🇻🇳 +84.<br/>- Bàn phím hiển thị: Numeric keyboard.<br/>- Placeholder số: *"Nhập số điện thoại"*.<br/><br/>**Quy tắc hành động:**<br/>- Tap vào phần prefix → Mở danh sách chọn quốc gia (Dropdown từ API danh mục, single-select, option đã chọn được highlight).<br/>- Khi đổi quốc gia → Cập nhật cờ và mã vùng. Với prefix **+84**: chấp nhận đầu số 03/05/07/08/09, đúng **9 chữ số**. Với prefix quốc gia khác: áp dụng độ dài linh hoạt theo chuẩn E.164 (từ **6 đến 15 chữ số**).<br/>- **Block input ký tự text:** Hệ thống chặn không cho nhập ký tự chữ cái và ký tự đặc biệt. Chỉ chấp nhận ký tự số (0–9). Hệ thống auto-trim số 0 ở phía đầu ô nhập số.<br/>- Trường này **bắt buộc**.<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống → *"Vui lòng nhập Số điện thoại!"*<br/>- Prefix +84: đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ"*<br/>- Nhập chưa đủ số lượng ký tự theo chuẩn quốc gia đã chọn → *"Số điện thoại nhập chưa đủ 9 ký tự!"*<br/>- Nhập quá số lượng ký tự theo chuẩn quốc gia đã chọn → *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09) |
| 4 | Loại tài khoản | Label (Read-only) | — | **Quy tắc hiển thị:**<br/>- Hiển thị cố định: **"Cá nhân"**. Không có ô nhập.<br/>- Không có viền input, không có nền tương tác.<br/><br/>**Quy tắc hành động:**<br/>- Không tap được, không chỉnh sửa được. |

**Section "Thông tin" (Collapsible — mặc định mở):**

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Mã định danh | Textbox (Read-only) | — | **Quy tắc hiển thị:**<br/>- Nền xám, viền disabled. Giá trị load từ hệ thống.<br/>- Không bao giờ null trên form chỉnh sửa (đã có khi đăng ký).<br/><br/>**Quy tắc hành động:**<br/>- Không chỉnh sửa được. Tap vào trường → Không mở bàn phím. |
| 2 | Ngày cấp | Textbox (Read-only) | — | **Quy tắc hiển thị:**<br/>- Nền xám, viền disabled. Định dạng: **DD/MM/YYYY** (CMR-12).<br/><br/>**Quy tắc hành động:**<br/>- Không chỉnh sửa được. Tap vào trường → Không mở bàn phím. |
| 3 | Nơi cấp | Textbox (Read-only) | — | **Quy tắc hiển thị:**<br/>- Nền xám, viền disabled. Nội dung dài → **wrap xuống dòng** trong ô (không truncate).<br/><br/>**Quy tắc hành động:**<br/>- Không chỉnh sửa được. Tap vào trường → Không mở bàn phím. |
| 4 | Mã số thuế | Textbox (Read-only) | — | **Quy tắc hiển thị:**<br/>- Nền xám, viền disabled.<br/><br/>**Quy tắc hành động:**<br/>- Không chỉnh sửa được. Tap vào trường → Không mở bàn phím. |
| 5 | Quốc gia | Dropdown | ✱ | **Quy tắc hiển thị:**<br/>- Đánh dấu (*) bên cạnh label.<br/>- Giá trị mặc định: load từ dữ liệu tài khoản hiện tại.<br/>- Danh sách từ API danh mục — không hard-code (CMR-03).<br/>- Placeholder: *"Chọn Quốc gia"*.<br/><br/>**Quy tắc hành động:**<br/>- Tap → Mở Bottom Sheet danh sách quốc gia (có ô tìm kiếm — Searchable, CMR-03). Chọn → Đóng, cập nhật giá trị.<br/>- Đổi Quốc gia → **Reset** Tỉnh/Thành phố và Phường/Xã về trống, đồng thời trigger gọi API load danh sách Tỉnh/Thành phố mới.<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống → *"Vui lòng chọn Quốc gia"* |
| 6 | Tỉnh/Thành phố | Dropdown (Searchable) | ✱ | **Quy tắc hiển thị:**<br/>- Đánh dấu (*) bên cạnh label.<br/>- Giá trị mặc định: load từ dữ liệu tài khoản hiện tại.<br/>- **Khi API đang load danh sách** (sau khi đổi Quốc gia): hiển thị spinner bên trong dropdown + dropdown ở trạng thái **disabled** (không tap được).<br/>- Sau khi load xong: chuyển về trạng thái enabled, hiển thị danh sách mới.<br/>- Placeholder: *"Chọn Tỉnh/Thành phố"*.<br/><br/>**Quy tắc hành động:**<br/>- **Disabled** nếu chưa chọn Quốc gia.<br/>- Tap → Mở danh sách dropdown (chỉ khi đã enabled). Chọn → Đóng, cập nhật giá trị.<br/>- Đổi Tỉnh/TP → **Reset** Phường/Xã về trống, trigger gọi API load danh sách Phường/Xã mới.<br/>- Xóa hết keyword trong ô tìm kiếm → hiển thị lại placeholder **"Tìm kiếm..."** (theo CMR-03).<br/>- Tap ra ngoài khi ô tìm kiếm trống → để rỗng, trigger validation bắt buộc (theo CMR-03).<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống → *"Vui lòng chọn Tỉnh/Thành phố"* |
| 7 | Phường/Xã | Dropdown (Searchable) | ✱ | **Quy tắc hiển thị:**<br/>- Đánh dấu (*) bên cạnh label.<br/>- Giá trị mặc định: load từ dữ liệu tài khoản hiện tại.<br/>- **Khi API đang load danh sách** (sau khi đổi Tỉnh/TP): hiển thị spinner bên trong dropdown + dropdown ở trạng thái **disabled**.<br/>- Sau khi load xong: chuyển về trạng thái enabled.<br/>- Placeholder: *"Chọn Phường/Xã"*.<br/><br/>**Quy tắc hành động:**<br/>- **Disabled** nếu chưa chọn Tỉnh/Thành phố.<br/>- Tap → Mở danh sách dropdown (chỉ khi đã enabled). Chọn → Đóng, cập nhật giá trị.<br/>- Xóa hết keyword trong ô tìm kiếm → hiển thị lại placeholder **"Tìm kiếm..."** (theo CMR-03).<br/>- Tap ra ngoài khi ô tìm kiếm trống → để rỗng, trigger validation bắt buộc (theo CMR-03).<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống → *"Vui lòng chọn Phường/Xã"* |
| 8 | Địa chỉ | Textbox | ✱ | **Quy tắc hiển thị:**<br/>- Đánh dấu (*) bên cạnh label.<br/>- Giá trị mặc định: load từ dữ liệu tài khoản hiện tại.<br/>- Cho phép nhập tự do: chữ, số, ký tự đặc biệt (số nhà, tên đường).<br/>- **Max length: 255 ký tự** (CMR-11).<br/>- Placeholder: *"Nhập Địa chỉ"*.<br/><br/>**Quy tắc hành động:**<br/>- Người dùng nhập địa chỉ. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Địa chỉ"*<br/>- Nhập quá 255 ký tự → *"Địa chỉ không được vượt quá 255 ký tự!"* (CMR-09) |
| 9 | Mã bưu chính | Textbox | — | **Quy tắc hiển thị:**<br/>- Không bắt buộc (không có dấu *).<br/>- Giá trị mặc định: load từ dữ liệu tài khoản hiện tại. Nếu chưa có → ô trống.<br/>- Placeholder: *"Nhập Mã bưu chính"*.<br/><br/>**Quy tắc hành động:**<br/>- Trường này **không bắt buộc**: nếu để trống → không validate, không báo lỗi.<br/>- Cho phép nhập: chữ, số (alphanumeric). Không chấp nhận ký tự đặc biệt. **Max length: 20 ký tự**.<br/>- Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/><br/>**Validation:**<br/>- Nhập ký tự đặc biệt → *"Mã bưu chính không hợp lệ"*<br/>- Nhập quá 20 ký tự → *"Mã bưu chính không được vượt quá 20 ký tự!"* |

**Khu vực nút hành động (Bottom — cố định):**

| # | Tên nút | Kiểu | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Lưu thay đổi | Button (Primary, full-width) | **Quy tắc hiển thị:**<br/>- Luôn hiển thị, luôn enabled.<br/><br/>**Quy tắc hành động:**<br/>- Tap → Validate toàn bộ form (bao gồm cả các trường trong section đang collapsed).<br/>- Nếu có lỗi → Hiển thị inline error dưới từng trường lỗi + tự động expand section đang collapsed có chứa lỗi. Không gọi API.<br/>- Nếu hợp lệ → Hiển thị loading indicator cục bộ → Gọi API cập nhật.<br/>- API thành công → Toast: *"Cập nhật thông tin tài khoản thành công!"* → Tự động quay về màn hình Xem chi tiết với dữ liệu mới nhất.<br/>- API trả lỗi trùng lặp: Nếu Email đã tồn tại → Toast: *"Email đã tồn tại"*. Nếu Số điện thoại đã tồn tại → Toast: *"Số điện thoại đã tồn tại"*. Giữ nguyên màn hình chỉnh sửa.<br/>- Có cơ chế debounce tránh double-tap (CMR-18). |
| 2 | Hủy | Button (Secondary, full-width) | **Quy tắc hiển thị:**<br/>- Luôn hiển thị, luôn enabled.<br/><br/>**Quy tắc hành động:**<br/>- Tap → Quay về màn hình Xem chi tiết ngay (không hiển thị dialog xác nhận). |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Xem chi tiết thông tin tài khoản cá nhân

**Main Flow:**
1. Người dùng tap "Thông tin cá nhân" từ màn hình Cấu hình tài khoản.
2. Hệ thống hiển thị full-screen loading overlay (CMR-07).
3. Gọi API lấy thông tin tài khoản → Ẩn loading → Hiển thị 2 section **Hồ sơ** và **Thông tin** (read-only). Field null → hiển thị "-".
4. Người dùng tap nút Edit (✏️) → Chuyển sang màn hình Chỉnh sửa.

**Error Flows:**
- **API fail (5xx):** Ẩn loading → Toast: *"Hệ thống đang bận. Vui lòng thử lại sau."* (CMR-07)
- **Timeout (>10s):** Toast: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + Nút "Thử lại". (CMR-07, CMR-16)
- **Mất mạng:** Toast: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + Nút "Thử lại". (CMR-07)
- **Session hết hạn (401):** Tự động dùng refresh token. Nếu refresh token hết hạn → Redirect về màn hình Đăng nhập + Toast: *"Phiên đăng nhập hết hạn."* (CMR-07)

**Pull-to-Refresh (CMR-13):**
- Kéo xuống từ đầu màn hình → Trigger gọi lại API lấy thông tin → Cập nhật dữ liệu.
- Nếu refresh thất bại → Giữ nguyên dữ liệu cũ + Toast lỗi (CMR-07).

---

#### 3.2 Xử lý Thu gọn / Mở rộng Section (Collapsible)

1. Màn hình Chỉnh sửa có 2 section: **Hồ sơ** và **Thông tin**, mặc định đều mở (expand).
2. Người dùng tap tiêu đề section (hoặc icon ^) → Section thu gọn / mở rộng xen kẽ.
3. Trạng thái thu gọn/mở rộng không ảnh hưởng đến dữ liệu đã nhập bên trong.
4. Khi validate lỗi: Nếu section đang collapsed mà có field lỗi bên trong → **Tự động expand** section đó để hiển thị lỗi.

---

#### 3.3 Xử lý Cập nhật thông tin tài khoản cá nhân

**Main Flow:**
1. Nút "Lưu thay đổi" luôn bật (enabled). Người dùng có thể nhấn Lưu ngay cả khi chưa chỉnh sửa trường dữ liệu nào.
2. Tap "Lưu thay đổi" (có debounce — CMR-18) → Validate toàn bộ form:
   - **Email:** Bắt buộc. Đúng định dạng email, tối đa 100 ký tự. Sai format → *"Email không đúng định dạng"*, quá ký tự → *"Email không được vượt quá 100 ký tự!"*.
   - **Số điện thoại:** Bắt buộc. Phải đúng độ dài theo quốc gia được chọn. Thiếu → *"Số điện thoại nhập chưa đủ 9 ký tự!"* (CMR-09); Thừa → *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09).
   - **Quốc gia, Tỉnh/TP, Phường/Xã, Địa chỉ:** Bắt buộc.
   - **Mã bưu chính:** Nếu nhập, chỉ cho phép chữ, số (không bao gồm khoảng trắng và ký tự có dấu), tối đa 20 ký tự.
3. Nếu có lỗi → Hiển thị inline error dưới trường tương ứng + Auto-expand section có lỗi. Không gọi API.
4. Validate thành công → Hiển thị loading indicator cục bộ → Gọi API cập nhật.
5. Thành công → Toast: *"Cập nhật thông tin tài khoản thành công!"* → Tự động quay về màn hình Xem chi tiết với dữ liệu mới nhất.
6. Thất bại do lỗi trùng lặp (từ API) → Toast: *"Email đã tồn tại"* hoặc *"Số điện thoại đã tồn tại"*. Giữ nguyên màn hình chỉnh sửa.
**Error Flows:**
- **API lưu fail (5xx):** Giữ nguyên dữ liệu đã nhập trên form. Toast: *"Hệ thống đang bận. Vui lòng thử lại sau."* (CMR-07)
- **Timeout (>10s):** Giữ nguyên dữ liệu đã nhập. Toast: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + Nút "Thử lại". (CMR-07)
- **Mất mạng:** Giữ nguyên dữ liệu đã nhập. Toast: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* (CMR-07)
- **Session hết hạn:** Redirect về Đăng nhập + Toast: *"Phiên đăng nhập hết hạn."* (CMR-07)


**Tác động cross-UC sau khi lưu thành công:**

> Khi Email hoặc Số điện thoại được thay đổi và lưu thành công, dữ liệu profile được cập nhật trên hệ thống. Tác động đến các màn hình khác như sau:

| UC | Màn hình | Trường bị ảnh hưởng | Hành vi | Kết luận |
|---|---|---|---|---|
| **UC64** | Form Tạo mới Phản ánh kiến nghị — Block "Thông tin cá nhân" | Email, Số điện thoại (auto-fill từ profile) | Khi user mở Form UC64 **sau khi** đã đổi Email/SĐT tại UC249 → Trường Email và SĐT được auto-fill với **giá trị mới nhất** từ profile. | ✅ Hành vi đúng — không cần fix. |
| **UC63** | Chi tiết Phản ánh kiến nghị — Block "Người gửi" | Email, Số điện thoại | Phản ánh đã nộp lưu snapshot tại thời điểm gửi. Thay đổi Email/SĐT ở UC249 **không làm cập nhật** các phản ánh cũ. | ✅ Hành vi đúng (immutable record) — không cần fix. |
| Các UC khác | UC1, UC2, UC40–90, UC229–260... | — | Không có màn hình nào đọc Email/SĐT từ profile user (đã scan toàn bộ 27 UC folder). | ✅ Không bị ảnh hưởng. |

---

#### 3.4 Xử lý Cascade Dropdown địa chỉ

1. Khi người dùng thay đổi **Quốc gia** → Tự động reset và load lại danh sách **Tỉnh/TP**. Đồng thời reset **Phường/Xã** về trống.
2. Khi người dùng thay đổi **Tỉnh/TP** → Tự động reset và load lại danh sách **Phường/Xã**.
3. Danh sách được lấy từ API danh mục — không hard-code (CMR-03).

**Error Flow khi cascade API fail:**
- Nếu API load Tỉnh/TP hoặc Phường/Xã thất bại (5xx / timeout / mất mạng) → Spinner biến mất, dropdown chuyển về trạng thái **enabled** (không còn disabled) → Toast lỗi theo CMR-07.
- Người dùng có thể tap lại dropdown để thử load lại.

#### 3.5 Đa ngôn ngữ (→ Xem CMR-17)

Toàn bộ text cứng trên màn hình UC249 (header, label trường thông tin, placeholder, nút "Lưu thay đổi"/"Hủy", thông báo lỗi validation, toast thành công/thất bại) được dịch sang ngôn ngữ hiển thị tương ứng khi người dùng đổi ngôn ngữ. Hỗ trợ 5 ngôn ngữ: VI, EN, ZH, JA, KO. Nội dung dữ liệu người dùng (họ tên, email, số điện thoại, địa chỉ) hiển thị nguyên bản — không thay đổi theo ngôn ngữ.

---

### 4. Acceptance Criteria

#### AC-01: Xem chi tiết thông tin tài khoản

| # | Tiêu chí | Pass condition |
|---|---|---|
| AC-01-1 | Màn hình tải thành công | Hiển thị full-screen loading khi gọi API. Sau khi nhận dữ liệu: 2 section Hồ sơ + Thông tin hiển thị đúng với dữ liệu tài khoản. |
| AC-01-2 | Field null hiển thị đúng | Mọi field có giá trị null từ API hiển thị "-". |
| AC-01-3 | Tất cả fields là read-only | Không có field nào cho phép chỉnh sửa trực tiếp trên màn hình Xem chi tiết. |
| AC-01-4 | Nút Edit hiển thị và hoạt động | Nút ✏️ hiển thị trên App Bar với mọi tài khoản Cá nhân. Tap → Mở màn hình Chỉnh sửa. |
| AC-01-5 | Pull-to-Refresh hoạt động | Kéo xuống → Spinner hiển thị → Dữ liệu mới nhất được tải lại. |
| AC-01-5b | Pull-to-Refresh thất bại | PTR thất bại (API fail / timeout / mất mạng) → Giữ nguyên dữ liệu cũ trên màn hình + Toast lỗi theo CMR-07. |
| AC-01-6 | Xử lý lỗi API | API fail / timeout / mất mạng → Hiển thị đúng message lỗi theo CMR-07. |

#### AC-02: Chỉnh sửa thông tin tài khoản

| # | Tiêu chí | Pass condition |
|---|---|---|
| AC-02-1 | Trạng thái nút "Lưu thay đổi" | Luôn enabled. |
| AC-02-2 | Họ và tên không chỉnh sửa được | Trường Họ và tên hiển thị nền xám, disabled. Tap vào trường → Không mở bàn phím, không cho nhập liệu. |
| AC-02-3 | Validation Email | Để trống → *"Vui lòng nhập Email"*. Nhập quá 100 ký tự → *"Email không được vượt quá 100 ký tự!"*. Sai định dạng → *"Email không đúng định dạng"*. |
| AC-02-4 | Validation SĐT | Bắt buộc — bỏ trống → *"Vui lòng nhập Số điện thoại!"*. Nhập ký tự chữ cái/đặc biệt → Hệ thống block, không cho nhập. Prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ"*. Nhập thiếu ký tự → *"Số điện thoại nhập chưa đủ 9 ký tự!"*. Nhập thừa ký tự → *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09). |
| AC-02-5 | Validation Mã bưu chính | Nhập ký tự có dấu / khoảng trắng / ký tự đặc biệt → *"Mã không bao gồm khoảng trắng và ký tự có dấu"*. Nhập quá 20 ký tự → *"Mã bưu chính không được vượt quá 20 ký tự!"*. |
| AC-02-6 | Auto-expand khi lỗi | Section đang collapsed có field lỗi → Tự động expand. |
| AC-02-7 | Lưu thành công | Toast *"Cập nhật thông tin tài khoản thành công!"* → Quay về Xem chi tiết với dữ liệu mới nhất. |
| AC-02-8 | Hủy chỉnh sửa | Tap nút Hủy → Quay về màn hình Xem chi tiết ngay (không hiển thị dialog xác nhận). |
| AC-02-9 | Xử lý lỗi khi lưu | API lưu fail → Giữ nguyên dữ liệu đã nhập + Toast lỗi đúng theo CMR-07. |
| AC-02-10 | Cascade Dropdown | Đổi Quốc gia → Reset Tỉnh/TP + Phường/Xã. Đổi Tỉnh/TP → Reset Phường/Xã. |
| AC-02-11 | Debounce | Double-tap nút ✏️ hoặc "Lưu thay đổi" không trigger 2 lần (CMR-18). |
| AC-02-12 | Lỗi trùng lặp Email/SĐT | Nhập Email hoặc SĐT đã tồn tại trên hệ thống → Lưu thay đổi → API báo lỗi → Hiển thị Toast *"Email đã tồn tại"* hoặc *"Số điện thoại đã tồn tại"*. Giữ nguyên dữ liệu trên màn hình Edit. |

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Nội dung cập nhật |
|---|---|---|
| 29/04/2026 | v1 | Khởi tạo |
| 11/05/2026 | v2 | Bổ sung màn hình Xem chi tiết, cấu trúc 2-section, các trường địa chỉ theo wireframe |
| 11/05/2026 | v2 | Bổ sung Preconditions/Postconditions, Acceptance Criteria, error flows, validation rules chi tiết theo BA Q&A |
| 11/05/2026 | v2 | Cập nhật Họ và tên: block input tại 100 ký tự (không cho nhập thêm) |
| 11/05/2026 | v2 | Cập nhật Cascade Dropdown: spinner bên trong dropdown khi API đang load Tỉnh/TP và Phường/Xã |
| 11/05/2026 | v2 → v2.1 | Bổ sung section đa ngôn ngữ (CMR-17): text cứng dịch 5 ngôn ngữ (VI, EN, ZH, JA, KO), nội dung dữ liệu người dùng giữ nguyên |
| 2026-05-12 | v2.1 → v2.2 | Cập nhật Null display format: `--` thành `-` (Đồng bộ CMR-14 v1.4) |
| 2026-05-12 | v2.1 → v2.2 | Cập nhật Inline error format: "Vui lòng nhập/chọn [field]." thành "[field] là bắt buộc." (Đồng bộ CMR-09 v1.4) |
| 2026-05-17 | v2.4 → v2.5 | CMR-09/CMR-03 — Chuẩn hoá required message: text→"Vui lòng nhập [tên]", dropdown→"Vui lòng chọn [tên]" (Đồng bộ CMR-09 v1.7) |
| 2026-05-13 | v2.2 → v2.3 | Email max length: Max 500 ký tự, block input (Đồng bộ CMR-11 default) |
| 2026-05-13 | v2.2 → v2.3 | Địa chỉ max length: Max 500 ký tự, block input (Đồng bộ CMR-11 default) |
| 2026-05-13 | v2.2 → v2.3 | Country Code Dropdown (SĐT prefix): Tường minh CMR-03: source API, searchable, single-select, highlight option đã chọn |
| 2026-05-13 | v2.2 → v2.3 | Section 3.4 — Cascade API fail: Error flow: Toast CMR-07 + dropdown re-enable sau khi API fail |
| 2026-05-13 | v2.2 → v2.3 | AC-01-5b — PTR fail: Giữ nguyên dữ liệu cũ + Toast CMR-07 khi PTR thất bại |
| 2026-05-13 | v2.2 → v2.3 | Section 3.3 — Tác động cross-UC: Bổ sung bảng tác động cross-UC (Phân tích W-03) |
| 2026-05-15 | v2.3 → v2.4 | Trường Họ và tên (form Chỉnh sửa): Chuyển sang Read-only (Label, nền xám, không chỉnh sửa được) — tương tự Mã định danh, Ngày cấp, Nơi cấp; xóa validation rules và cập nhật AC-02-2 |

| 2026-05-18 | v2.5 → v2.6 | Cập nhật Toast message sau chỉnh sửa TK thành công: "Cập nhật thông tin thành công." → "Cập nhật thông tin tài khoản thành công!"<br/>Theo Feedback BA |
| 2026-05-18 | v2.6 → v2.7 | Email validation: Đổi message sai format "Sai định dạng." → "Email không đúng định dạng" (tất cả case)<br/>Theo Feedback BA |
| 2026-05-18 | v2.6 → v2.7 | SĐT: Bổ sung rule block input ký tự text (chỉ chấp nhận số 0-9, xóa validate on-blur cho ký tự không phải số)<br/>Theo Feedback BA |
| 2026-05-18 | v2.6 → v2.7 | Quốc gia: Bỏ searchable (ô tìm kiếm), giữ Dropdown mở Bottom Sheet danh sách từ API<br/>Theo Feedback BA |
| 2026-05-18 | v2.7 → v2.8 | SĐT: Chuyển thành trường bắt buộc (✱). Tách validation message: thiếu ký tự → "Số điện thoại nhập chưa đủ 9 ký tự!", thừa ký tự → "Số điện thoại nhập quá ký tự cho phép", bỏ trống → "Vui lòng nhập Số điện thoại!". Bỏ message cũ "Sai định dạng."<br/>Theo Feedback BA |
| 2026-05-18 | v2.8 → v2.9 | Email: Xóa dòng "Bàn phím hiển thị Email keyboard", bỏ hành vi block input khi đạt 500 ký tự, thay bằng validation message "Email không được vượt quá 100 ký tự!" (Đồng bộ CMR-09)<br/>Conflict CMR-09 |
| 2026-05-18 | v2.9 → v2.10 | Địa chỉ: Bỏ hành vi block input khi đạt 500 ký tự, thay bằng validation message "Địa chỉ không được vượt quá 255 ký tự!" (Đồng bộ CMR-09)<br/>Conflict CMR-09 |
| 2026-05-18 | v2.10 → v2.11 | Cập nhật version metadata |
| 2026-05-19 | v2.11 → v2.12 | Email: max 500 → 100 ký tự (đồng bộ UC250). SĐT: bổ sung rule E.164 tường minh (+84: đầu số 03/05/07/08/09, 9 chữ số; quốc tế: 6–15 chữ số). Mã bưu chính: thêm max 20 ký tự + error "Mã bưu chính không được vượt quá 20 ký tự!". |
| 2026-05-19 | v2.12 → v2.13 | Dropdown (Quốc gia, Tỉnh/TP, Phường/Xã): Sửa trigger validation thành hiển thị lỗi ngay khi rời khỏi trường. |
| 2026-05-19 | v2.13 → v2.14 | Bỏ tính năng searchable ở ô chọn prefix SĐT quốc gia theo feedback. |
| 2026-05-19 | v2.14 → v2.15 | Bổ sung quy tắc Disabled trường Tỉnh/TP và Phường/Xã nếu chưa chọn cấp cha (Đồng bộ UC250). |
| 2026-05-19 | v2.15 → v2.16 | SĐT: bổ sung case validation prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ"*. Cập nhật AC-02-4. |
| 2026-05-20 | v2.16 → v2.17 | Cập nhật quy tắc: Nút Lưu và Hủy luôn enable. |
| 2026-05-21 | v2.17 → v2.18 | Bổ sung Toast lỗi trùng lặp Email/Số điện thoại. Sửa inline error Email rỗng thành *"Vui lòng nhập địa chỉ email"* theo chuẩn web. |
| 2026-05-21 | v2.18 → v2.19 | Bổ sung quy tắc auto-trim số 0 ở đầu trường Số điện thoại. |
| 2026-05-21 | v2.17 → v2.20 | Align CMR Mobile v6.0 | 1. Địa chỉ max 500→255. 2. Error format CMR-09. 3. Bỏ dấu "." cuối inline errors. 4. Thêm rule CMR-11 cho Mã bưu chính. 5. Error required SĐT thêm "!". |
| 2026-05-21 | v2.20 → v2.21 | SĐT — Error max length | *"Số điện thoại nhập quá ký tự cho phép"* → *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09) |
| 2026-05-21 | v2.21 → v2.22 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v2.22 → v2.23 | Align CMR Mobile v6.0 | 1. Thêm "khi out-click" cho auto-trim (Email, Địa chỉ, Mã BC). 2. Chuẩn rule B05 cho Mã BC. 3. Chuẩn D07, D08 cho Dropdown (Tỉnh/TP, Phường/Xã). 4. Chuẩn H01 cho Email (bỏ "địa chỉ"). |
