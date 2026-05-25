# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC250 — Quản lý tài khoản doanh nghiệp trên Mobile
**Ngày tạo:** 13/05/2026
**Phiên bản:** v3.20
**Cập nhật:** 21/05/2026 — v3.19: Align CMR-09 v6.0: max length 3 trường, B05 rule Mã định danh, thêm `!` vào error required.

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Quản lý tài khoản |
| Đối tượng thực hiện | Tổ chức / Doanh nghiệp (đã đăng nhập) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 13/05/2026 |
| Phiên bản | v3.19 |

> **Phạm vi UC này:** Chỉ áp dụng cho tài khoản loại **Tổ chức / Doanh nghiệp**. Tài khoản **Cá nhân** được xử lý ở màn hình riêng (UC249).

---

## UC250 — Quản lý tài khoản doanh nghiệp trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Quản lý tài khoản doanh nghiệp trên Mobile
- **Mô tả:** Chức năng cho phép người dùng xem toàn bộ thông tin tài khoản tổ chức/doanh nghiệp và chỉnh sửa một số trường thông tin khác. Gồm 2 tab chính: "Thông tin định danh" (Read-only) và "Thông tin khác" (View Mode & Edit Mode).
- **Phân quyền:** Tổ chức / Doanh nghiệp đã đăng nhập. (User Cá nhân không có quyền truy cập vào màn hình này).
- **Phạm vi ngoài UC (Exclusions):** UC này KHÔNG bao gồm: quản lý thông tin tài khoản **Cá nhân** (UC249), cấu hình tài khoản (UC254), đổi mật khẩu (UC251).
- **Truy cập chức năng:** Sidebar → **"Cấu hình tài khoản"** → Tap **"Tài khoản doanh nghiệp"**.
- **Điều kiện tiên quyết (Preconditions):** Người dùng đã đăng nhập vào ứng dụng. Loại tài khoản là **Tổ chức / Doanh nghiệp**.
- **Điều kiện kết thúc (Postconditions):** Thông tin tài khoản được lưu xuống DB với dữ liệu mới nhất. Session không bị ảnh hưởng.
- **Chức năng đáp ứng usecase số:** UC250 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Quản lý tài khoản doanh nghiệp (UC250)

**Mô tả giao diện:**
App bar có Title là "Tài khoản doanh nghiệp". Màn hình có 2 tab: "Thông tin định danh" và "Thông tin khác". 

**Tab 1: Thông tin định danh (Read-only) - Tab mặc định (Default)**
App bar ở Tab này chỉ có nút Back (←), KHÔNG có nút Edit. Thông tin định danh không được phép chỉnh sửa. Hỗ trợ Pull-to-Refresh (CMR-13).
**Quy tắc hành vi nút Back:** Tap → Quay về màn hình trước.

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Banner Info | Banner | | **Quy tắc hiển thị:** Text: *"Thông tin định danh không thể chỉnh sửa. Nếu có sai sót, vui lòng liên hệ hỗ trợ."*<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 2 | Loại tài khoản | Label | | **Quy tắc hiển thị:** Label "Tổ chức / Doanh nghiệp".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 3 | Tên tổ chức | Label | | **Quy tắc hiển thị:** Hiển thị giá trị từ hệ thống. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 4 | Mã số thuế | Label | | **Quy tắc hiển thị:** Hiển thị giá trị từ hệ thống. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 5 | Mã định danh | Label | | **Quy tắc hiển thị:** Hiển thị giá trị từ hệ thống. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 6 | Ngày cấp | Label | | **Quy tắc hiển thị:** Định dạng dd/MM/yyyy. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 7 | Nơi cấp | Label | | **Quy tắc hiển thị:** Hiển thị giá trị từ hệ thống. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |

---

**Tab 2: Thông tin khác (View Mode & Edit Mode)**

**A. Chế độ View (Mặc định khi mở Tab 2):**
- App bar có nút Back (←) và Nút Edit (✏️).
- Các phần thông tin được chia thành phần có thể thu gọn (Collapsible). **Trạng thái mặc định: Expand (Mở rộng) tất cả các section.**
- Dữ liệu hiển thị dạng read-only label. **Quy tắc hiển thị chung:** Đối với các trường văn bản dài (địa chỉ, tên tổ chức, nơi cấp...), nếu độ dài text vượt quá chiều ngang màn hình thì tự động **wrap (xuống dòng)**, KHÔNG hiển thị dấu ba chấm (truncate).

**Section "Thông tin tổ chức" (View mode):**

| # | Tên trường | Kiểu trường | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Tên tổ chức (English) | Label | **Quy tắc hiển thị:** Hiển thị giá trị từ hệ thống. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 2 | Tên viết tắt | Label | **Quy tắc hiển thị:** Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 3 | Quyết định thành lập | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 4 | Giấy chứng nhận đầu tư | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 5 | Quốc gia | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 6 | Quốc tịch | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 7 | Tỉnh/Thành phố | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 8 | Phường/Xã | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 9 | Địa chỉ | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 10 | Mã bưu chính | Label | **Quy tắc hiển thị:** Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 11 | Số điện thoại | Label | **Quy tắc hiển thị:** Hiển thị kèm mã vùng (VD: +84 024-3456-7890). Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 12 | Email chính thức của tổ chức | Label | **Quy tắc hiển thị:** Hiển thị tối đa **1 dòng**, quá dài **truncate (…)** ở cuối. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |

**Section "Thông tin người đại diện" (View mode):**

| # | Tên trường | Kiểu trường | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Họ và tên | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 2 | Chức vụ / Chức danh | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 3 | Ngày sinh | Label | **Quy tắc hiển thị:** Định dạng dd/MM/yyyy.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 4 | Mã định danh người đại diện | Label | **Quy tắc hiển thị:** Hiển thị giá trị.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 5 | Ngày cấp | Label | **Quy tắc hiển thị:** Định dạng dd/MM/yyyy.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 6 | Nơi cấp | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 7 | Số điện thoại | Label | **Quy tắc hiển thị:** Hiển thị kèm mã vùng.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 8 | Email | Label | **Quy tắc hiển thị:** Hiển thị tối đa **1 dòng**, quá dài **truncate (…)** ở cuối. Nếu rỗng hiển thị "-".<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |
| 9 | Địa chỉ | Label | **Quy tắc hiển thị:** Hiển thị giá trị. Nếu rỗng hiển thị "-". Wrap xuống dòng nếu quá dài.<br/>**Quy tắc hành động:** Read-only.<br/>**Validation:** N/A |

---

**B. Chế độ Edit:**
- Khi nhấn nút Edit (✏️), màn hình chuyển sang chế độ Nhập liệu.
- Dưới cùng xuất hiện khu vực Button Sticky Bottom (Lưu thay đổi / Hủy).
- **Quy tắc hiển thị lỗi chung:** Lỗi validation hiển thị **ngay khi người dùng rời khỏi trường** (focus out / chuyển sang trường khác / tap ra ngoài). Không chờ đến khi nhấn "Lưu thay đổi". Thông báo lỗi hiển thị inline màu đỏ, ngay dưới trường tương ứng (CMR-09).

**App Bar:**

| # | Thành phần | Kiểu | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Nút Back (←) | Icon Button | **Quy tắc hiển thị:**<br/>- Luôn hiển thị ở góc trái header (CMR-06).<br/><br/>**Quy tắc hành động:**<br/>- Tap → Quay về chế độ View. |

**Section "Thông tin tổ chức" (Collapsible — mặc định mở):**

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Tên tổ chức (English) | Textbox | | **Quy tắc hiển thị:** Label: "Tên tổ chức (Tiếng anh)". Placeholder: *"Nhập Tên tổ chức (Tiếng anh)"*. **Max length: 255 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Tên tổ chức. Không dấu. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Trường này **không bắt buộc**: nếu để trống → không validate, không báo lỗi. Nhập quá 255 ký tự → *"Tên tổ chức (Tiếng anh) không được vượt quá 255 ký tự!"* (CMR-09). |
| 2 | Tên viết tắt | Textbox | | **Quy tắc hiển thị:** Label: "Tên viết tắt". Placeholder: *"Nhập Tên viết tắt"*. **Max length: 255 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Tên viết tắt. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Nhập quá 255 ký tự → *"Tên viết tắt không được vượt quá 255 ký tự!"* (CMR-09). |
| 3 | Quyết định thành lập | Textbox | | **Quy tắc hiển thị:** Label: "Quyết định thành lập". Placeholder: *"Nhập Quyết định thành lập"*. **Max length: 50 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Quyết định thành lập. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Nhập quá 50 ký tự → *"Quyết định thành lập không được vượt quá 50 ký tự!"* (CMR-09). |
| 4 | Giấy chứng nhận đầu tư | Textbox | | **Quy tắc hiển thị:** Label: "Giấy chứng nhận đầu tư". Placeholder: *"Nhập Giấy chứng nhận đầu tư"*. **Max length: 50 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Giấy chứng nhận đầu tư. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Nhập quá 50 ký tự → *"Giấy chứng nhận đầu tư không được vượt quá 50 ký tự!"* (CMR-09). |
| 5 | Quốc gia | Dropdown | ✱ | **Quy tắc hiển thị:** Searchable (CMR-03). Placeholder: *"Chọn Quốc gia"*.<br/>**Quy tắc hành động:** Tap → Mở Bottom sheet danh sách từ API (có ô tìm kiếm). Chọn → Đóng, cập nhật giá trị.<br/>**Cascade Logic:** Đổi Quốc gia → **Reset** Tỉnh/Thành phố và Phường/Xã về trống, đồng thời trigger gọi API load danh sách Tỉnh/Thành phố mới.<br/>- Xóa hết keyword trong ô tìm kiếm → hiển thị lại placeholder **"Chọn Quốc gia"** (theo CMR-03).<br/>- Tap ra ngoài khi ô tìm kiếm trống → để rỗng, trigger validation bắt buộc (theo CMR-03).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng chọn Quốc gia"*. |
| 6 | Quốc tịch | Dropdown | ✱ | **Quy tắc hiển thị:** Có thanh Search bar (CMR-03). Placeholder: *"Chọn Quốc tịch"*.<br/>**Quy tắc hành động:** Tap → Mở Bottom sheet danh sách từ API. Chọn → Đóng, cập nhật giá trị.<br/>- Xóa hết keyword trong ô tìm kiếm → hiển thị lại placeholder **"Chọn Quốc tịch"** (theo CMR-03).<br/>- Tap ra ngoài khi ô tìm kiếm trống → để rỗng, trigger validation bắt buộc (theo CMR-03).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng chọn Quốc tịch"*. |
| 7 | Tỉnh/Thành phố | Dropdown | ✱ | **Quy tắc hiển thị:** Searchable (CMR-03). Placeholder: *"Chọn Tỉnh/Thành phố"*.<br/>**Quy tắc hành động:** **Disabled** nếu chưa chọn Quốc gia. **Khi API đang load** (sau khi đổi Quốc gia): hiển thị spinner bên trong dropdown + dropdown ở trạng thái **disabled** (không tap được). Sau khi load xong: chuyển về trạng thái enabled, hiển thị danh sách mới. Tap → Mở danh sách dropdown (chỉ khi đã enabled). Chọn → Đóng, cập nhật giá trị.<br/>**Cascade Logic:** Đổi Tỉnh/Thành → **Reset** Phường/Xã về trống, trigger gọi API load danh sách Phường/Xã mới.<br/>**Behavior khi lỗi API:** Spinner biến mất, dropdown chuyển về trạng thái enabled để user có thể tap thử load lại. Toast lỗi CMR-07.<br/>- Xóa hết keyword trong ô tìm kiếm → hiển thị lại placeholder **"Chọn Tỉnh/Thành phố"** (theo CMR-03).<br/>- Tap ra ngoài khi ô tìm kiếm trống → để rỗng, trigger validation bắt buộc (theo CMR-03).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng chọn Tỉnh/Thành phố"*. |
| 8 | Phường/Xã | Dropdown | ✱ | **Quy tắc hiển thị:** Searchable (CMR-03). Placeholder: *"Chọn Phường/Xã"*.<br/>**Quy tắc hành động:** **Disabled** nếu chưa chọn Tỉnh/Thành. **Khi API đang load** (sau khi đổi Tỉnh/Thành): hiển thị spinner bên trong dropdown + dropdown ở trạng thái **disabled**. Sau khi load xong: chuyển về trạng thái enabled. Tap → Mở danh sách dropdown (chỉ khi đã enabled). Chọn → Đóng, cập nhật giá trị.<br/>**Behavior khi lỗi API:** Spinner biến mất, dropdown chuyển về trạng thái enabled để user có thể tap thử load lại. Toast lỗi CMR-07.<br/>- Xóa hết keyword trong ô tìm kiếm → hiển thị lại placeholder **"Chọn Phường/Xã"** (theo CMR-03).<br/>- Tap ra ngoài khi ô tìm kiếm trống → để rỗng, trigger validation bắt buộc (theo CMR-03).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng chọn Phường/Xã"*. |
| 9 | Địa chỉ | Textbox | ✱ | **Quy tắc hiển thị:** Label "Địa chỉ". Placeholder: *"Nhập Địa chỉ"*. **Max length: 255 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Cho phép nhập tự do: chữ, số, ký tự đặc biệt (số nhà, tên đường). Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Địa chỉ"*. Nhập quá 255 ký tự → *"Địa chỉ không được vượt quá 255 ký tự!"* (CMR-09). |
| 10 | Mã bưu chính | Textbox | | **Quy tắc hiển thị:** Label "Mã bưu chính". Placeholder: *"Nhập Mã bưu chính"*. **Max length: 20 ký tự** (CMR-09).<br/>**Quy tắc hành động:** Trường này **không bắt buộc**: nếu để trống → không validate, không báo lỗi. Cho phép nhập tự do: chữ, số(alphanumeric). Không chấp nhận ký tự đặc biệt. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation:**<br/>- Nhập ký tự đặc biệt → *"Mã bưu chính không hợp lệ"*<br/>- Nhập quá 20 ký tự → *"Mã bưu chính không được vượt quá 20 ký tự!"* | |
| 11 | Số điện thoại (Tổ chức) | Textbox (tel) + Country Code Prefix | ✱ | **Quy tắc hiển thị:**<br/>- Ô nhập gồm 2 phần: **[Cờ quốc gia + Mã vùng]** (prefix, bên trái) và **[Ô nhập số]** (bên phải).<br/>- Mặc định: 🇻🇳 +84.<br/>- Bàn phím hiển thị: Numeric keyboard.<br/>- Placeholder số: *"Nhập số điện thoại"*.<br/><br/>**Quy tắc hành động:**<br/>- Tap vào phần prefix → Mở danh sách chọn quốc gia (Dropdown từ API danh mục, single-select, option đã chọn được highlight).<br/>- Khi đổi quốc gia → Cập nhật cờ và mã vùng. Với prefix **+84**: chấp nhận đầu số 03/05/07/08/09, đúng **9 chữ số**. Với prefix quốc gia khác: áp dụng độ dài linh hoạt theo chuẩn E.164 (từ **6 đến 15 chữ số**).<br/>- **Block input ký tự text:** Hệ thống chặn không cho nhập ký tự chữ cái và ký tự đặc biệt. Chỉ chấp nhận ký tự số (0–9). Hệ thống auto-trim số 0 ở phía đầu ô nhập số.<br/>- Trường này **bắt buộc**.<br/><br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*:<br/>- Để trống → *"Vui lòng nhập Số điện thoại!"*<br/>- Prefix +84: đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ"*<br/>- Nhập chưa đủ số lượng ký tự theo chuẩn quốc gia đã chọn → *"Số điện thoại nhập chưa đủ 9 ký tự!"* (CMR-09)<br/>- Nhập quá số lượng ký tự theo chuẩn quốc gia đã chọn → *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09) |
| 12 | Email chính thức của tổ chức | Textbox | ✱ | **Quy tắc hiển thị:** Placeholder: *"Nhập Email chính thức"*. **Max length: 100 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Email chính thức. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập địa chỉ email"*. Không có ký tự @ → *"Email không đúng định dạng"*. Không có phần domain (VD: abc@) → *"Email không đúng định dạng"*. Không có phần extension (VD: abc@domain) → *"Email không đúng định dạng"*. Có khoảng trắng giữa chuỗi (VD: abc @gmail.com) → *"Email không đúng định dạng"*. Nhập quá 100 ký tự → *"Email chính thức không được vượt quá 100 ký tự!"* (CMR-09). |

**Section "Thông tin người đại diện" (Collapsible — mặc định mở):**

| # | Tên trường | Kiểu trường | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|
| 1 | Họ và tên | Textbox | ✱ | **Quy tắc hiển thị:** Label "Họ và tên". Placeholder: *"Nhập Họ và tên"*. **Max length: 255 ký tự** (CMR-09).<br/>**Quy tắc hành động:** Người dùng nhập Họ và tên. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Họ và tên!"*. Nhập quá 255 ký tự → *"Họ và tên không được vượt quá 255 ký tự!"* (CMR-09). |
| 2 | Chức vụ / Chức danh | Textbox | ✱ | **Quy tắc hiển thị:** Label "Chức vụ / Chức danh". Placeholder: *"Nhập Chức vụ / Chức danh"*. **Max length: 50 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Chức vụ / Chức danh. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Chức vụ / Chức danh"*. Nhập quá 50 ký tự → *"Chức vụ / Chức danh không được vượt quá 50 ký tự!"* (CMR-09). |
| 3 | Ngày sinh | Datepicker | ✱ | **Quy tắc hiển thị:** Định dạng dd/MM/yyyy. Placeholder: *"Chọn ngày sinh"*.<br/>**Quy tắc hành động:** Chọn ngày. Max date: Hôm nay.<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng nhập ngày sinh"*. |
| 4 | Mã định danh người đại diện | Textbox | ✱ | **Quy tắc hiển thị:** Label "Mã định danh người đại diện". Placeholder: *"Nhập Mã định danh người đại diện"*. **Max length: 12 ký tự** (CMR-09).<br/>**Quy tắc hành động:** Bàn phím số (numeric keyboard). Chỉ chấp nhận ký tự số (0–9). Auto-trim. Không cho phép khoảng trắng và ký tự tiếng Việt có dấu (CMR-09 B05).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng nhập Mã định danh người đại diện"*. Có khoảng trắng hoặc ký tự có dấu → *"Mã không bao gồm khoảng trắng và ký tự có dấu"* (CMR-09). Nhập quá 12 ký tự → *"Mã định danh không được vượt quá 12 ký tự!"*. |
| 5 | Ngày cấp | Datepicker | ✱ | **Quy tắc hiển thị:** Định dạng dd/MM/yyyy. Placeholder: *"Chọn ngày cấp"*.<br/>**Quy tắc hành động:** Chọn ngày. Max date: Hôm nay. Min date: 01/01/1900.<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng nhập ngày cấp"*. |
| 6 | Nơi cấp | Textbox | ✱ | **Quy tắc hiển thị:** Label "Nơi cấp". Placeholder: *"Nhập Nơi cấp"*. **Max length: 255 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Người dùng nhập Nơi cấp. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Nơi cấp"*. Nhập quá 255 ký tự → *"Nơi cấp không được vượt quá 255 ký tự!"* (CMR-09). |
| 7 | Số điện thoại (Người ĐD) | Textbox | ✱ | **Quy tắc hiển thị:** Bàn phím hiển thị: Numeric keyboard. Placeholder: *"Nhập số điện thoại"*.<br/>**Quy tắc hành động:** Cho phép nhập ký tự số (0–9) và duy nhất một dấu cộng (+) ở vị trí đầu tiên. **Chặn (block input) hoàn toàn** ký tự chữ cái, khoảng trắng (space) và các ký tự đặc biệt khác. Nếu user copy-paste chuỗi có khoảng trắng/ký tự đặc biệt hoặc nhiều dấu `+` (VD: `++090-123 456`), hệ thống tự động loại bỏ các ký tự không hợp lệ và chỉ giữ lại số (cùng 1 dấu `+` ở đầu nếu có). Hệ thống auto-trim số 0 ở phía đầu trường SĐT (sau dấu + nếu có).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống → *"Vui lòng nhập Số điện thoại"*.<br/>— **Case 1 – Nhập số Việt Nam định dạng nội địa (Bắt đầu bằng 0, sau đó bị trim đi 0):** Kiểm tra ký tự bắt đầu của chuỗi (sau khi đã trim số 0) phải thuộc các đầu số hợp lệ (3, 5, 7, 8, 9) và tổng độ dài chuỗi chính xác là 9 chữ số.<br/>— **Case 2 – Nhập số Việt Nam định dạng quốc tế (Bắt đầu bằng +84):** Kiểm tra phần sau +84 bắt đầu bằng 3, 5, 7, 8, 9 và có đúng 9 chữ số (tổng chuỗi là 12 ký tự).<br/>— **Case 3 – Nhập số Quốc tế khác (Bắt đầu bằng + và khác +84):** Áp dụng chuẩn E.164, độ dài từ 6 đến 15 chữ số (không tính dấu cộng).<br/>— **Thông báo lỗi:** Sai đầu số VN / Không đúng chuẩn → *"Số điện thoại không hợp lệ"*. Chưa đủ ký tự → *"Số điện thoại nhập chưa đủ 9 ký tự!"* (CMR-09). Quá ký tự → *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09). |
| 8 | Email | Textbox | ✱ | **Quy tắc hiển thị:** Label "Email". Placeholder: *"Nhập Email"*. **Max length: 100 ký tự** (CMR-09).<br/>**Quy tắc hành động:** Người dùng nhập Email. Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Email"*. Không có ký tự @ → *"Email không đúng định dạng"*. Không có phần domain (VD: abc@) → *"Email không đúng định dạng"*. Không có phần extension (VD: abc@domain) → *"Email không đúng định dạng"*. Có khoảng trắng giữa chuỗi (VD: abc @gmail.com) → *"Email không đúng định dạng"*. Nhập quá 100 ký tự → *"Email không được vượt quá 100 ký tự!"*. |
| 9 | Địa chỉ | Textbox | ✱ | **Quy tắc hiển thị:** Label "Địa chỉ". Placeholder: *"Nhập Địa chỉ"*. **Max length: 255 ký tự** (CMR-11).<br/>**Quy tắc hành động:** Cho phép nhập tự do: chữ, số, ký tự đặc biệt (số nhà, tên đường). Hệ thống auto-trim khoảng trắng đầu/cuối (CMR-09).<br/>**Validation** *(hiển thị lỗi ngay khi rời khỏi trường)*: Để trống hoặc chỉ nhập khoảng trắng → *"Vui lòng nhập Địa chỉ"*. Nhập quá 255 ký tự → *"Địa chỉ không được vượt quá 255 ký tự!"* (CMR-09). |

**Khu vực nút hành động (Bottom sticky trong chế độ Edit):**

| # | Tên nút | Kiểu | Mô tả/Ghi chú |
|---|---|---|---|
| 1 | Lưu thay đổi | Button (Primary) | **Quy tắc hiển thị:** **Luôn Enabled** (nền đỏ đậm).<br/>**Quy tắc hành động:** Tap → Validate toàn bộ form (bao gồm cả các trường trong section đang collapsed). Nếu có lỗi → Hiển thị inline error dưới từng trường lỗi + tự động expand section đang collapsed có chứa lỗi. Không gọi API. Nếu hợp lệ → Hiển thị loading indicator cục bộ → Gọi API.<br/>— **API thành công:** Toast *"Cập nhật thông tin tài khoản thành công!"* → Về màn View.<br/>— **API trả lỗi SĐT/Email trùng:** Nếu Số điện thoại đã tồn tại trên hệ thống → Hiển thị Toast lỗi *"Số điện thoại đã tồn tại"*. Nếu Email đã tồn tại → Hiển thị Toast lỗi *"Email đã tồn tại"*. Giữ nguyên màn Edit, không reset form.<br/>— **API lỗi khác (5xx/timeout/mất mạng):** Toast lỗi theo CMR-07.<br/>Có cơ chế debounce (CMR-18). |
| 2 | Hủy | Button (Secondary) | **Quy tắc hiển thị:** **Luôn Enabled**.<br/>**Quy tắc hành động:** Tap → Về màn View (không hiển thị dialog xác nhận). |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Thu gọn / Mở rộng Section (Collapsible)
1. Màn hình có 2 section: "Thông tin tổ chức" và "Thông tin người đại diện", mặc định đều mở (expand).
2. Người dùng tap tiêu đề section → Section thu gọn / mở rộng xen kẽ.
3. Khi validate lỗi: Nếu section đang collapsed mà có field lỗi bên trong → **Tự động expand** section đó để hiển thị lỗi.

#### 3.2 Xử lý Xem/Sửa thông tin tài khoản
- **Cascade Dropdown địa chỉ:** Đổi Quốc gia → tự động gọi API load Tỉnh/Thành và reset Phường/Xã. Đổi Tỉnh/Thành → load Phường/Xã mới. Nếu lỗi API (5xx/timeout/mất mạng) → Spinner biến mất, dropdown chuyển về trạng thái enabled để user có thể tap thử load lại. Toast lỗi CMR-07.
- **Error Flows API:** Mất mạng/Timeout/5xx → Hiển thị Toast lỗi theo CMR-07.
- **Debounce:** Nút Lưu, Hủy, Edit có cơ chế chống double tap (CMR-18).
- **Hành vi nút Back (App Bar) ở chế độ Edit:** 
  - Tap Back → về chế độ View.
- **Pull-to-refresh (CMR-13):** Tại Tab Thông tin định danh / Thông tin khác (chế độ xem), vuốt kéo xuống để refresh API mới nhất.

#### 3.3 Đa ngôn ngữ (CMR-17)
Toàn bộ text tĩnh trên màn hình (header, label, placeholder, error message inline, toast text) dịch tự động theo 5 ngôn ngữ: VI, EN, ZH, JA, KO dựa trên cấu hình App. Dữ liệu nhập của user giữ nguyên văn bản gốc.

---

### 4. Acceptance Criteria

| # | Tiêu chí | Pass condition |
|---|---|---|
| AC-01 | Quyền truy cập UC250 | Màn hình Quản lý tài khoản doanh nghiệp chỉ hiển thị/cho phép truy cập đối với User có loại tài khoản là Tổ chức/Doanh nghiệp. |
| AC-02 | Chuyển Tab | Tap Tab 1/Tab 2 màn hình chuyển tab thành công, hiển thị đúng data. |
| AC-03 | Format Inline Error | Lỗi hiển thị ngay dưới trường khi focus out, text hiển thị đúng chuẩn "Vui lòng nhập/chọn [tên trường]" hoặc "Sai định dạng". |
| AC-04 | Dropdown Cascade | Đổi Quốc gia → Reset Tỉnh/TP + Phường/Xã. Đổi Tỉnh/Thành -> Trường Phường/Xã ngay lập tức bị reset trống. |
| AC-05 | Nút Back (Edit mode) | Mở màn Edit -> Bấm Back → Về màn View. Bấm Hủy → Về màn View ngay. |
| AC-06 | Pull To Refresh | Kéo màn hình (khi View) -> Spinner hiển thị -> Data refresh. Rớt mạng -> Toast CMR-07. |
| AC-07 | Nút Lưu thay đổi — Luôn Enabled | Khi mở màn Edit, nút "Lưu thay đổi" luôn ở trạng thái Enabled (nền đỏ đậm). |
| AC-08 | Nút Hủy — Luôn Enabled | Nút "Hủy" luôn ở trạng thái Enabled. |
| AC-09 | Validation Chức vụ / Chức danh | Nhập quá 50 ký tự → Inline error *"Chức vụ / Chức danh không được vượt quá 50 ký tự!"*. |
| AC-10 | Validation Mã định danh người ĐD | Nhập quá 12 chữ số → Inline error *"Mã định danh không được vượt quá 12 ký tự!"*. (Hệ thống đã tự động block ký tự không phải số). |
| AC-11 | Validation Nơi cấp người ĐD | Nhập quá 255 ký tự → Inline error *"Nơi cấp không được vượt quá 255 ký tự!"*. |
| AC-12 | Validation SĐT (+84) | Prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 → inline error *"Số điện thoại không hợp lệ"*. Nhập chưa đủ ký tự → inline error *"Số điện thoại nhập chưa đủ 9 ký tự!"* (CMR-09). Nhập quá ký tự → inline error *"Số điện thoại không được vượt quá 9 ký tự!"* (CMR-09). |
| AC-13 | Cross-UC — UC64 auto-fill | Sau khi lưu thành công UC250, mở Form UC64 (Phản ánh kiến nghị) -> Trường SĐT và Email của block "Thông tin tổ chức" tự động điền giá trị mới nhất từ profile. |
| AC-14 | Cross-UC — UC1 Card thông tin | Sau khi lưu thành công UC250, quay về Trang chủ (UC1) -> Card thông tin người dùng hiển thị đúng Tên tổ chức (nếu có thay đổi) và Vai trò. |
| AC-15 | Toast lỗi SĐT/Email đã tồn tại | Nhập SĐT hoặc Email Tổ chức / Người đại diện trùng với dữ liệu đã có trên hệ thống → Nhấn Lưu → API trả lỗi → Toast *"Số điện thoại đã tồn tại"* hoặc *"Email đã tồn tại"* hiển thị. Giữ nguyên màn Edit, không reset form. |

---

### 5. Tác động cross-UC sau khi lưu thành công

> Khi thông tin tài khoản doanh nghiệp được lưu thành công, dữ liệu profile được cập nhật trên hệ thống. Tác động đến các màn hình khác:

| UC | Màn hình | Trường bị ảnh hưởng | Hành vi | Kết luận |
|---|---|---|---|---|
| **UC64** | Form Tạo mới Phản ánh kiến nghị — Block "Thông tin tổ chức" | SĐT, Email (auto-fill từ profile) | Khi user mở Form UC64 **sau khi** đã đổi SĐT/Email tại UC250 → Trường SĐT và Email được auto-fill với **giá trị mới nhất** từ profile. | ✅ Hành vi đúng — không cần fix. |
| **UC63** | Chi tiết Phản ánh kiến nghị — Block "Người gửi" | SĐT, Email | Phản ánh đã nộp lưu snapshot tại thời điểm gửi. Thay đổi SĐT/Email ở UC250 **không làm cập nhật** các phản ánh cũ. | ✅ Hành vi đúng (immutable record) — không cần fix. |
| **UC1** | Trang chủ — Card thông tin người dùng | Tên tổ chức, Vai trò | Khi user quay lại Trang chủ, Card thông tin được refresh từ API → hiển thị Tên tổ chức mới nhất. | ✅ Hành vi đúng — UC1 đã có cơ chế refresh mỗi lần vào Tab. |
| Các UC khác | UC2, UC40–90, UC229–260... | — | Không có màn hình nào đọc trực tiếp SĐT/Email/Tên tổ chức từ profile DN (đã scan toàn bộ UC folder). | ✅ Không bị ảnh hưởng. |

---

### 6. Lịch sử cập nhật

| Ngày | Phiên bản | Nội dung cập nhật |
|---|---|---|
| 13/05/2026 | v1.0 | Khởi tạo tài liệu (Tách từ UC250-253_QuanLyTaiKhoan v3.4). Chuẩn hóa format. |
| 14/05/2026 | v1.0 → v2.0 | Q1: Chức vụ/Chức danh — bổ sung max 50 ký tự, auto-trim |
| 14/05/2026 | v1.0 → v2.0 | Q2: Mã định danh người ĐD — bổ sung numeric keyboard, chỉ ký tự số, max 50 ký tự |
| 14/05/2026 | v1.0 → v2.0 | Q3: Nơi cấp người ĐD — bổ sung max 500 ký tự (theo CMR-11) |
| 14/05/2026 | v1.0 → v2.0 | Q4: SĐT Tổ chức & Người ĐD — bổ sung chi tiết: đầu số 03/05/07/08/09, đúng 9 số sau +84; prefix quốc tế theo chuẩn quốc tế |
| 14/05/2026 | v1.0 → v2.0 | Q5: Bổ sung Section 5 — Tác động cross-UC (UC64, UC63, UC1) sau khi lưu thành công |
| 14/05/2026 | v1.0 → v2.0 | Q6: Nút Lưu thay đổi — cập nhật logic: Disabled khi chưa đổi HOẶC còn lỗi validation; Enabled khi có thay đổi VÀ toàn bộ hợp lệ |
| 14/05/2026 | v1.0 → v2.0 | Bổ sung AC-07 đến AC-14 tương ứng các câu hỏi Q1–Q6 |
| 14/05/2026 | v2.0 → v3.0 | Chuẩn hóa format 3 quy tắc cho View/Edit Tab 1 & Tab 2. Cập nhật logic SĐT (dropdown API, chuẩn E.164). |
| 14/05/2026 | v3.0 → v3.1 | Validation Max Length (13 trường)<br/>Vượt quá [X] ký tự -> "Tối đa [X] ký tự."<br/>Tối đa [X] ký tự, nếu vượt quá, block nhập<br/>Đồng bộ chuẩn Block input (CMR-01/11) thay vì hiển thị inline error. |
| 17/05/2026 | v3.1 → v3.2 | CMR-09/CMR-03 — Chuẩn hoá required message toàn bộ Edit section: text→"Vui lòng nhập", dropdown/datepicker→"Vui lòng chọn"<br/>Đồng bộ CMR-09 v1.6 |
| 18/05/2026 | v3.2 → v3.3 | Tab 2 — Edit mode — Section "Thông tin tổ chức": Đổi 2 trường "Tên tổ chức (English)" và "Tên viết tắt" sang Textbox Disabled (read-only, không cho chỉnh sửa). |
| 19/05/2026 | v3.3 → v3.4 | Đổi "Tên tổ chức (English)" và "Tên viết tắt" từ Disabled → Enabled. Bổ sung ✱ required. Bổ sung placeholder CMR-09/CMR-03. Fix date format, null handling. |
| 19/05/2026 | v3.4 → v3.5 | C4: Địa chỉ max → inline error *"Địa chỉ không được vượt quá 255 ký tự!"*. C5+C8: Email max → inline error, format → *"Email không đúng định dạng"*. C7: Toast → *"Cập nhật thông tin tài khoản thành công!"*. C9: Quốc gia bỏ searchable. C10: Hủy → không hiển thị dialog. Đồng bộ UC249. |
| 19/05/2026 | v3.5 → v3.6 | SĐT tách 2-case validation (*"chưa đủ ký tự"* / *"quá ký tự"*). Mã bưu chính: bỏ numeric keyboard, sửa rule chỉ chặn ký tự đặc biệt (cho phép chữ cái). Quốc gia/Tỉnh/TP/Phường/Xã: trigger validate khi submit. Tỉnh/TP + Phường/Xã: thêm spinner loading state khi API cascade. Nút Lưu: Enabled khi có ít nhất 1 thay đổi (validate khi bam Luu). |
| 19/05/2026 | v3.7 → v3.8 | Đồng bộ 100% chuẩn UI/UX, validation triggers, max length rules, popup logic từ UC249. Chuẩn hóa format bảng Edit mode. |
| 19/05/2026 | v3.8 → v3.9 | Dropdown địa chỉ: bổ sung hành vi retry khi lỗi API. Sửa AC-04. Xóa câu báo lỗi "Mã định danh không hợp lệ" do đã block nhập (Đồng bộ UC249). |
| 19/05/2026 | v3.9 → v3.10 | SĐT Tổ chức và SĐT Người ĐD: bổ sung case validation prefix +84 nhưng đầu số không thuộc 03/05/07/08/09 → *"Số điện thoại không hợp lệ"*. Cập nhật AC-12. |
| 19/05/2026 | v3.10 → v3.11 | Mã định danh người đại diện: sửa max 50 ký tự → max 12 chữ số. Cập nhật §2.2 (Edit mode) và AC-10. |
| 20/05/2026 | v3.11 → v3.12 | Cập nhật nút "Lưu thay đổi" và "Hủy" luôn Enabled. Sửa đổi AC-07 và AC-08 tương ứng. |
| 20/05/2026 | v3.12 → v3.13 | Bổ sung Toast lỗi *"Số điện thoại đã tồn tại"* khi API trả lỗi trùng SĐT (áp dụng cả SĐT Tổ chức và SĐT Người đại diện). Bổ sung AC-15. |
| 21/05/2026 | v3.13 → v3.14 | Cập nhật error message rỗng cho các trường Email và Thông tin người đại diện theo chuẩn Web. Bổ sung validate trùng lặp cho Email (hiển thị Toast *"Email đã tồn tại"*). |
| 21/05/2026 | v3.14 → v3.15 | Bổ sung quy tắc auto-trim số 0 ở đầu trường Số điện thoại Tổ chức và Số điện thoại Người đại diện. |
| 21/05/2026 | v3.15 → v3.16 | Sửa trường Tên tổ chức (English) thành không bắt buộc theo QC feedback. Đồng bộ format mô tả trường Số điện thoại (Tổ chức) giống UC249. Làm rõ behavior block khoảng trắng và nhiều dấu + ở SĐT Người đại diện. |
| 2026-05-21 | v3.13 → v3.17 | Align CMR Mobile v6.0 | 1. Nơi cấp max 500→255. 2. Khai báo max 255 cho Tên tổ chức/Tên viết tắt. 3. Error format CMR-09. 4. Bỏ dấu "." cuối inline errors. 5. Thêm rule CMR-11 cho Mã định danh. 6. Error required SĐT thêm "!". |
| 2026-05-21 | v3.17 → v3.18 | SĐT/Email — Error max/min length | Format cũ "nhập quá/chưa đủ ký tự cho phép" → format CMR-09 (CMR-09) |
| 2026-05-21 | v3.18 → v3.19 | Align CMR-09 — Fix 6 lỗi error max-length còn sót | Dòng 114 (Tên tổ chức EN), 115 (Tên viết tắt), 116 (QĐ thành lập), 117 (GCNĐT), 125 (Email chính thức), 131 (Họ và tên): `"nhập quá ký tự cho phép"` → `"không được vượt quá [N] ký tự!"` (CMR-09). |
| 2026-05-21 | v3.19 → v3.20 | Align CMR-09 v6.0 | 1. Họ và tên (Người ĐD): max 255. 2. Email (Người ĐD): chuẩn hóa max 100. 3. Mã bưu chính: max 20 + validation. 4. Mã định danh người ĐD: chuẩn hóa max 12 + B05 rule. 5. Xóa dấu ! thừa ở các dropdown. |
| 2026-05-21 | v3.20 → v3.21 | Bổ sung D07/D08 CMR-03 | Bổ sung behavior: Xóa hết keyword → placeholder (D07) và Tap ra ngoài → rỗng + trigger validation (D08) cho 4 Searchable Dropdown form: Quốc gia, Quốc tịch, Tỉnh/Thành phố, Phường/Xã. |
