# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC62 — Tra cứu Doanh nghiệp trên Mobile  
**Ngày tạo:** 12/05/2026  
**Phiên bản:** v1.0

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | hieu.luu2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Tra cứu thông tin Doanh nghiệp / Kết nối giao thương |
| Đối tượng thực hiện | Nhà đầu tư, Người dùng chung (Cá nhân / Tổ chức) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 12/05/2026 |
| Phiên bản | v1.0 |

---

## UC62 — Tra cứu Doanh nghiệp trên Mobile

### 1. Mô tả chức năng
- **Tên chức năng:** Tra cứu Doanh nghiệp (Kết nối giao thương).
- **Mô tả:** Chức năng đóng vai trò như một danh bạ doanh nghiệp, giúp nhà đầu tư và người dùng tra cứu thông tin của các công ty, đối tác tiềm năng. Người dùng có thể tìm kiếm theo tên, ngành nghề, và lọc qua bộ lọc chi tiết (quy mô, tỉnh thành, nhu cầu kết nối). Màn hình "Hồ sơ doanh nghiệp" cung cấp cái nhìn toàn cảnh về công ty, bao gồm các chỉ số nổi bật, sản phẩm chủ lực, nhu cầu hợp tác và thông tin liên hệ.
- **Phân quyền:** Public access (Không yêu cầu đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** Các đường link liên hệ như Website hay Email trên màn hình hồ sơ chỉ gọi ra Intent của hệ điều hành, hệ thống không lưu log gửi mail hay log click nội bộ.
- **Truy cập chức năng:** Trang chủ → "Kết nối giao thương" (Danh bạ doanh nghiệp).
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị danh sách công ty hoặc hồ sơ chi tiết một công ty cụ thể.
- **Chức năng đáp ứng usecase số:** UC62

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Doanh nghiệp

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header | Button & Label | "Kết nối giao thương" | — | — | **Quy tắc hiển thị:** Nền đỏ đậm. Dòng phụ nhỏ "Danh bạ Doanh nghiệp" ở dưới tiêu đề chính. Kèm icon Quay lại và icon Thông báo (chuông). |
| 2 | Ô tìm kiếm | Searchbox | "Tìm tên công ty, ngành nghề..." | x | — | **Quy tắc hành động:** Kích hoạt API tìm kiếm với debounce 3s, tự động cắt khoảng trắng (CMR-01). |
| 3 | Nút Bộ lọc | Button (Icon) | — | — | — | Kế bên ô tìm kiếm, tap mở Bottom Sheet Bộ lọc (CMR-02). |
| 4 | Trạng thái hiển thị & Tag bộ lọc | Tag Group | — | — | — | Hiển thị "6 doanh nghiệp" (ví dụ). Cạnh đó là nhóm các Tag bộ lọc đang áp dụng (VD: "Tất cả", "Đã xác minh"). |
| 5 | Danh sách Thẻ Công ty | List Card | — | — | — | **Quy tắc hiển thị:** Lazy load 20 thẻ (CMR-04), Pull to refresh (CMR-13), Empty State khi không có data (CMR-14). |
| 6 | Thẻ Công ty | Card Box | — | — | — | **Mỗi thẻ bao gồm:**<br>- **Logo / Avatar:** Ô vuông bo góc hiển thị tên viết tắt (VD: ABC trên nền xanh) hoặc logo thực tế.<br>- **Tên công ty:** Chữ in đậm. Có thể đi kèm icon tick xanh (Verified) nếu tài khoản đã xác minh.<br>- **Thông tin:** Ngành nghề (VD: Sản xuất vật liệu), Quy mô (100-500 nhân sự), Vị trí (Hà Nội).<br>- **Tag "Đang tìm":** Nền xám mờ (VD: Nhà phân phối, Đối tác sản xuất).<br>- **Nút "Xem chi tiết >"**: Viền đỏ mờ chữ đỏ. |
| 7 | Tương tác Thẻ | Interaction | — | — | — | Tap vào toàn bộ thẻ hoặc nút "Xem chi tiết" → Mở màn hình Hồ sơ doanh nghiệp (Debounce chống click đúp CMR-18). |

---

#### 2.2 Bottom Sheet Bộ lọc tìm kiếm

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header Bộ lọc | Label | "Bộ lọc tìm kiếm" | — | — | Có nút X ở góc để đóng popup. Dòng hướng dẫn nền cam nhạt. |
| 2 | Ngành nghề kinh doanh | Dropdown | "Chọn ngành nghề" | x | — | Danh sách lấy theo API hệ thống (Tham chiếu chuẩn dropdown CMR-03). |
| 3 | Nhu cầu kết nối | Dropdown | "Tất cả nhu cầu" | x | — | VD: Tìm nhà cung cấp, Tìm nhà phân phối, Tìm vốn... (CMR-03). |
| 4 | Quy mô nhân sự | Dropdown | "Tất cả quy mô" | x | — | VD: 10-50, 50-100, 100-500... (CMR-03). |
| 5 | Tỉnh / Thành phố | Dropdown | "Toàn quốc" | x | — | Load danh sách tỉnh thành (CMR-03). |
| 6 | Nút chức năng | Button Group | — | — | — | **Thiết lập lại:** Xóa điều kiện, trả về mặc định.<br>**Áp dụng:** Đóng sheet, tải lại danh sách với tham số mới. |

---

#### 2.3 Màn hình Hồ sơ doanh nghiệp

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header | Button & Label | "Hồ sơ doanh nghiệp" | — | — | Header đỏ đậm, chữ trắng. Cố định phía trên khi cuộn. |
| 2 | Khối Profile trên cùng | Profile Box | — | — | — | Bao gồm: Logo to ở giữa, Tên công ty (có icon tick xanh nếu Verified), Mã số thuế màu xám, và Badge ngành nghề viền xanh (VD: `# Sản xuất vật liệu xây dựng`). |
| 3 | Highlight Thông số | List Attribute | — | — | — | 3 cột chỉ số nền trắng, số liệu đỏ đậm:<br>- **Năm thành lập** (VD: 2015)<br>- **Nhân sự** (VD: 320+)<br>- **Phạm vi** (VD: 5 tỉnh) |
| 4 | Khối 1: Tổng quan | Attribute Group | — | — | — | Nhóm thông tin chi tiết: Năm thành lập, Loại hình (VD: Công ty Cổ phần), Địa chỉ, Quy mô. Riêng dòng **Website** hiển thị dạng text link màu xanh gạch chân. Tap vào mở OS Default Browser. |
| 5 | Khối 2: Năng lực & Nhu cầu | Section Group | — | — | — | **Nhu cầu kết nối:** Nằm trong khung viền đỏ nhạt, text mô tả chi tiết yêu cầu tìm kiếm đối tác.<br>**Sản phẩm / Dịch vụ chính:** Danh sách dạng Tag Pills (VD: Gạch ốp lát, Đá nhân tạo...).<br>**Tag thành tựu:** (Thường nằm cuối khối), VD "Tăng trưởng 30%/năm" (màu xanh lá), "Xuất khẩu 5 nước" (màu xanh dương). |
| 6 | Khối 3: Thông tin liên hệ | Section Group | — | — | — | Hiển thị: Người đại diện (VD: Nguyễn Văn Minh) kèm icon User.<br>Hiển thị: Email (Text link màu xanh gạch chân). Tap vào mở App Mail mặc định (`mailto://`). |

---

### 3. Mô tả các xử lý của chức năng

1. **Tìm kiếm & Lọc (CMR-01):**
   - Ô search tự động cắt khoảng trắng đầu/cuối. Gọi API tìm kiếm sau **3 giây** ngừng gõ (Debounce).
   - Có cơ chế **State Persistence**: Khi user cuộn danh sách xuống trang số 3, xem chi tiết 1 hồ sơ rồi ấn Back, giao diện List phải duy trì đúng bộ lọc, text tìm kiếm và vị trí scroll hiện tại.
2. **Logic icon "Đã xác minh" (Verified Tick):**
   - Dựa vào trường `isVerified = true/false` từ API. Nếu `true`, hiển thị icon tick xanh biển cạnh tên công ty (cả ngoài List và trong chi tiết).
3. **Hiển thị Avatar/Logo công ty:**
   - Nếu API trả về ảnh logo hợp lệ, hệ thống render ảnh qua Cache Image.
   - Nếu lỗi load ảnh hoặc API không có ảnh, hệ thống tự động fallback sinh Avatar dạng Text (VD: Lấy tối đa 3 ký tự đầu tiên của tên viết tắt, chữ trắng trên nền khối màu như thiết kế).
4. **Call Intent Hệ điều hành (OS Intent):**
   - Mở Website (Khối Tổng quan): Sử dụng Intent Web Browser mặc định (Chrome/Safari) khi user tap vào link có định dạng hợp lệ.
   - Gửi Email (Khối Liên hệ): Kích hoạt Intent `mailto://[email]`. Thiết bị tự động mở ứng dụng gửi mail với địa chỉ người nhận đã được điền sẵn.
5. **Xử lý Exception ngầm định (CMR-04 & CMR-07):**
   - Lazy load ở trang List tự retry 3 lần ngầm cách nhau 2s nếu bị lỗi mạng. Quá 3 lần mới hiện cảnh báo.
   - Nếu một trong các khối của màn Chi tiết (Ví dụ khối Năng lực) bị lỗi API, áp dụng cơ chế Partial Failure: Vẫn hiển thị Khối Tổng quan và Khối Liên hệ, phần lỗi hiển thị Empty State.

---

### 4. Tiêu chí chấp nhận (AC)
- **AC1:** Tìm kiếm văn bản có Debounce 3s, tự trim khoảng trắng (CMR-01). Mọi filter (Bottom sheet) áp dụng chính xác lên danh sách kết quả.
- **AC2:** Giao diện thẻ công ty render đúng UI: Fallback avatar text nếu mất ảnh logo, hiển thị đúng tick Verified nếu tài khoản đã xác thực.
- **AC3:** Thao tác xem hồ sơ chi tiết chuyển màn mượt mà, chống click đúp (CMR-18).
- **AC4:** State Persistence hoạt động đúng 100%. Khi Back từ màn hình chi tiết, list phải giữ nguyên vị trí cuộn và các tiêu chí lọc.
- **AC5:** Các đường link Website, Email ở màn Chi tiết gọi thành công đến ứng dụng trình duyệt hoặc mail Native của OS. Nếu máy không có App xử lý email, ứng dụng hiển thị thông báo "Không tìm thấy ứng dụng email" thay vì crash.
- **AC6:** Lazy load 20 công ty mỗi lần cuộn xuống. Empty state hiển thị chuẩn UX dự án khi list trống (CMR-14).

---

### 5. Lịch sử cập nhật
| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 12/05/2026 | v1.0 | Tạo mới | (Không có) | Tạo mới tài liệu SRS UC62 | Phân tích từ 3 màn hình wireframe: List, Filter, Chi tiết. Chuẩn hóa hành vi UI theo CMR hiện hành. |
