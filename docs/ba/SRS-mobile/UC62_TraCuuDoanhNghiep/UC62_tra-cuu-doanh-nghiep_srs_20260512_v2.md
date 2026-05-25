# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC62 — Tra cứu Doanh nghiệp trên Mobile  
**Ngày tạo:** 12/05/2026  
**Phiên bản:** v2.4

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | hieu.luu2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Tra cứu thông tin Doanh nghiệp / Kết nối giao thương |
| Đối tượng thực hiện | Nhà đầu tư, Người dùng chung (Cá nhân / Tổ chức) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 12/05/2026 |
| Phiên bản | v2.4 |

---

## UC62 — Tra cứu Doanh nghiệp trên Mobile

### 1. Mô tả chức năng
- **Tên chức năng:** Tra cứu Doanh nghiệp (Kết nối giao thương).
- **Mô tả:** Chức năng đóng vai trò như một danh bạ doanh nghiệp, giúp nhà đầu tư và người dùng tra cứu thông tin của các công ty, đối tác tiềm năng. Người dùng có thể tìm kiếm theo tên, ngành nghề, và lọc qua bộ lọc chi tiết (quy mô, tỉnh thành, nhu cầu kết nối) hoặc lọc nhanh bằng quick-filter trên danh sách. Màn hình "Hồ sơ doanh nghiệp" cung cấp cái nhìn toàn cảnh về công ty, bao gồm các chỉ số nổi bật, sản phẩm chủ lực, nhu cầu hợp tác và thông tin liên hệ.
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
| 1 | Header | Button & Label | "Kết nối giao thương" | — | — | **Quy tắc hiển thị:** Nền đỏ đậm. Dòng phụ nhỏ "Danh bạ Doanh nghiệp" ở dưới tiêu đề chính. Kèm icon Quay lại. |
| 2 | Ô tìm kiếm | Searchbox | "Tìm kiếm nhanh theo tên công ty, ngành nghề" | x | — | **Quy tắc hiển thị:** Tối đa **255 ký tự** (Tham chiếu CMR-01).<br>**Quy tắc hành động:** Kích hoạt API tìm kiếm với debounce 3s, tự động cắt khoảng trắng (CMR-01). Ô tìm kiếm kết hợp với Quick Filter hiện tại — kết quả phải thỏa cả hai điều kiện (CMR-01). Khi chuyển sang màn hình khác → Reset search/filter về trạng thái mặc định (CMR-01). State Persistence: Giữ nguyên từ khóa khi quay lại từ màn hình chi tiết (CMR-01). |
| 3 | Nút Bộ lọc | Button (Icon) | — | — | — | Kế bên ô tìm kiếm, tap mở Bottom Sheet Bộ lọc (CMR-02). |
| 4 | Trạng thái hiển thị & Tag bộ lọc nhanh (Quick Filter) | Tag Group | "Tất cả" | — | — | Hiển thị dòng đếm số lượng (VD: "6 doanh nghiệp").<br>Bên phải là cụm Tag ngang: `Tất cả` và `Đã xác minh`.<br>**Quy tắc hành động:** Đây là nút **Quick-filter**. Tap vào `Đã xác minh` hệ thống sẽ gọi API lọc lại danh sách ngay lập tức để chỉ hiện công ty có tick xanh (không cần qua popup Bộ lọc). |
| 5 | Danh sách Thẻ Công ty | List Card | — | — | — | **Quy tắc hiển thị:** Lazy load 20 thẻ (CMR-04), Pull to refresh (CMR-13). Empty State: API trả về danh sách rỗng → "Không có dữ liệu" / Search-filter không kết quả → "Không tìm thấy kết quả" (CMR-14). |
| 6 | Thẻ Công ty | Card Box | — | — | — | **Mỗi thẻ bao gồm:**<br>- **Logo / Avatar:** Ô vuông bo góc hiển thị tên viết tắt (VD: ABC trên nền xanh) hoặc logo thực tế.<br>- **Tên công ty:** Chữ in đậm. Có thể đi kèm icon tick xanh (Verified) nếu tài khoản đã xác minh.<br>- **Thông tin:** Ngành nghề (VD: Sản xuất vật liệu), Quy mô (100-500 nhân sự), Vị trí (Hà Nội).<br>- **Tag "Đang tìm":** Nền xám mờ. Dữ liệu string hiển thị trên thẻ này map trực tiếp 1-1 với **tên Option trong Dropdown Nhu cầu kết nối** của hệ thống (VD: "Nhà phân phối", "Đối tác sản xuất").<br>- **Nút "Xem chi tiết >"**: Viền đỏ mờ chữ đỏ. |
| 7 | Tương tác Thẻ | Interaction | — | — | — | Tap vào toàn bộ thẻ hoặc nút "Xem chi tiết" → Mở màn hình Hồ sơ doanh nghiệp (Debounce chống click đúp CMR-18). |

---

#### 2.2 Bottom Sheet Bộ lọc tìm kiếm

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header Bộ lọc | Label | "Bộ lọc tìm kiếm" | — | — | Có nút X ở góc để đóng popup. Dòng hướng dẫn nền cam nhạt. |
| 2 | Ngành nghề kinh doanh | Dropdown (Searchable) | "Tất cả" | x | — | Danh sách lấy theo API hệ thống (Tham chiếu CMR-03, D07/D08).<br>Xóa hết keyword → hiển thị lại placeholder "Tất cả". Tap ra ngoài khi trống → chọn lại "Tất cả". Khi nhập keyword không có option trùng khớp → hiển thị "Không có dữ liệu" (CMR-03). |
| 3 | Nhu cầu kết nối | Dropdown (Searchable) | "Tất cả" | x | — | VD: Tìm nhà cung cấp, Tìm nhà phân phối, Tìm vốn... (CMR-03, D07/D08).<br>Xóa hết keyword → hiển thị lại placeholder "Tất cả". Tap ra ngoài khi trống → chọn lại "Tất cả". Khi nhập keyword không có option trùng khớp → hiển thị "Không có dữ liệu" (CMR-03). |
| 4 | Quy mô nhân sự | Dropdown | "Tất cả" | x | — | VD: 10-50, 50-100, 100-500... (CMR-03). |
| 5 | Tỉnh / Thành phố | Dropdown (Searchable) | "Tất cả" | x | — | Load danh sách tỉnh thành (CMR-03, D07/D08).<br>Xóa hết keyword → hiển thị lại placeholder "Tất cả". Tap ra ngoài khi trống → chọn lại "Tất cả". Khi nhập keyword không có option trùng khớp → hiển thị "Không có dữ liệu" (CMR-03). |
| 6 | Nút chức năng | Button Group | — | — | — | **Thiết lập lại:** Xóa điều kiện, trả về mặc định.<br>**Áp dụng:** **Luôn Enabled** (CMR-09). Không có trạng thái Disabled. Tap → Đóng sheet, tải lại danh sách với tham số mới. |

---

#### 2.3 Màn hình Hồ sơ doanh nghiệp

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header | Button & Label | "Hồ sơ doanh nghiệp" | — | — | Header đỏ đậm, chữ trắng. Cố định phía trên khi cuộn. |
| 2 | Khối Profile trên cùng | Profile Box | — | — | — | Bao gồm: Logo to ở giữa, Tên công ty (có icon tick xanh nếu Verified), Mã số thuế màu xám, và Badge ngành nghề viền xanh (VD: `# Sản xuất vật liệu xây dựng`). |
| 3 | Highlight Thông số | List Attribute | — | — | — | 3 cột chỉ số nền trắng, số liệu đỏ đậm:<br>- **Năm thành lập** (VD: 2015)<br>- **Nhân sự** (VD: 320+)<br>- **Phạm vi** (VD: 5 tỉnh) |
| 4 | Khối 1: Tổng quan | Attribute Group | — | — | — | Nhóm thông tin chi tiết: Năm thành lập, Loại hình, Địa chỉ, Quy mô.<br>**Trường Website:**<br>- Nếu có dữ liệu: Hiển thị text link màu xanh gạch chân. Tap mở OS Default Browser.<br>- Nếu không có dữ liệu: Hiển thị dấu gạch ngang `-` và **Disable click**. |
| 5 | Khối 2: Năng lực & Nhu cầu | Section Group | — | — | — | **Nhu cầu kết nối:** Nằm trong khung viền đỏ nhạt, text diễn giải mô tả yêu cầu tìm kiếm (văn bản dài).<br>**Sản phẩm / Dịch vụ chính:** Danh sách dạng Tag Pills (VD: Gạch ốp lát, Đá nhân tạo...). Nếu số lượng Tag quá dài vượt quá giới hạn khung nhìn (Ví dụ vượt quá 3 dòng hiển thị), hệ thống sẽ gộp lại và hiển thị nút **"Xem thêm"**.<br>**Tag thành tựu:** VD "Tăng trưởng 30%/năm" (xanh lá), "Xuất khẩu 5 nước" (xanh dương). |
| 6 | Khối 3: Thông tin liên hệ | Section Group | — | — | — | Hiển thị: Người đại diện (VD: Nguyễn Văn Minh) kèm icon User.<br>**Trường Email:**<br>- Nếu có dữ liệu: Text link màu xanh gạch chân. Tap mở App Mail mặc định (`mailto://`).<br>- Nếu không có dữ liệu: Hiển thị dấu gạch ngang `-` và **Disable click**. |

---

### 3. Mô tả các xử lý của chức năng

1. **Tìm kiếm & Lọc (CMR-01):**
   - Ô search tự động cắt khoảng trắng đầu/cuối. Gọi API tìm kiếm sau **3 giây** ngừng gõ (Debounce).
   - Có cơ chế **State Persistence**: Khi user cuộn danh sách xuống trang số 3, xem chi tiết 1 hồ sơ rồi ấn Back, giao diện List phải duy trì đúng bộ lọc (gồm popup Filter và Quick-filter), text tìm kiếm và vị trí scroll hiện tại.
2. **Logic icon "Đã xác minh" (Verified Tick):**
   - Dựa vào trường `isVerified = true/false` từ API. Nếu `true`, hiển thị icon tick xanh biển cạnh tên công ty (cả ngoài List và trong chi tiết).
3. **Hiển thị Avatar/Logo công ty:**
   - Nếu API trả về ảnh logo hợp lệ, hệ thống render ảnh qua Cache Image.
   - Nếu lỗi load ảnh hoặc API không có ảnh, hệ thống tự động fallback sinh Avatar dạng Text (VD: Lấy tối đa 3 ký tự đầu tiên của tên viết tắt, chữ trắng trên nền khối màu như thiết kế).
4. **Call Intent Hệ điều hành (OS Intent) & Handle Dữ liệu trống:**
   - Nếu thông tin liên hệ (Website, Email) chưa cập nhật, field đó sẽ bị disable click và điền chuỗi `-`.
   - Nếu có thông tin, sử dụng Intent tương ứng (OS Browser, App Mail) để xử lý.
5. **Xử lý Exception ngầm định (CMR-04 & CMR-07):**
   - **First-load:** Sử dụng loading state toàn màn hình (full-screen loading overlay) cho lần tải đầu tiên (CMR-07).
   - **Lazy load:** Tự retry 3 lần ngầm cách nhau 2s nếu bị lỗi mạng. Quá 3 lần mới hiện cảnh báo (CMR-04).
   - **Timeout API (>10s):** Hiển thị thông báo *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại"* kèm nút "Thử lại" (CMR-07/CMR-16).
   - Nếu một trong các khối của màn Chi tiết (Ví dụ khối Năng lực) bị lỗi API, áp dụng cơ chế Partial Failure: Vẫn hiển thị Khối Tổng quan và Khối Liên hệ, phần lỗi hiển thị Empty State.

---

### 4. Tiêu chí chấp nhận (AC)
- **AC1:** Tìm kiếm văn bản có Debounce 3s, tự trim khoảng trắng (CMR-01). Mọi filter (Bottom sheet) và Quick-filter trên thanh điều hướng ("Đã xác minh") áp dụng chính xác lên danh sách kết quả.
- **AC2:** Giao diện thẻ công ty render đúng UI: Fallback avatar text nếu mất ảnh logo, hiển thị đúng tick Verified nếu tài khoản đã xác thực. Nhãn "Đang tìm" hiển thị đúng keyword (ngắn) map với Dropdown Category.
- **AC3:** Thao tác xem hồ sơ chi tiết chuyển màn mượt mà, chống click đúp (CMR-18).
- **AC4:** State Persistence hoạt động đúng 100%. Khi Back từ màn hình chi tiết, list phải giữ nguyên vị trí cuộn và các tiêu chí lọc.
- **AC5:** Các đường link Website, Email ở màn Chi tiết gọi thành công đến ứng dụng trình duyệt hoặc mail Native của OS. Đối với trường hợp data rỗng, hệ thống hiển thị dấu `-` và không cho phép click.
- **AC6:** Khối Tag "Sản phẩm / Dịch vụ" phải tự động gom nhóm và hiển thị nút "Xem thêm" nếu số lượng vượt quá không gian màn hình thiết kế.

---

### 5. Lịch sử cập nhật
| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 12/05/2026 | v1.0 | Tạo mới | (Không có) | Tạo mới tài liệu SRS UC62 | Phân tích từ 3 màn hình wireframe: List, Filter, Chi tiết. Chuẩn hóa hành vi UI theo CMR hiện hành. |
| 12/05/2026 | v2.0 | Giải quyết Gaps Audit | Chưa rõ logic hiển thị Tag và data rỗng | - Làm rõ "Đã xác minh" là Quick-filter<br>- "Đang tìm" lấy option ngắn từ Dropdown<br>- "Sản phẩm" có giới hạn nút Xem thêm<br>- Dữ liệu liên hệ trống hiển thị "-" và disable | Update theo QnA |
| 2026-05-21 | v2.0 → v2.1 | Align CMR Mobile v6.0 | 1. Search box thiếu max length. 2. Dropdown thiếu D07/D08. | 1. Bổ sung max 255 ký tự cho ô tìm kiếm (E05). 2. Bổ sung hành vi clear keyword D07/D08 cho Searchable Dropdown. | Rà soát theo Align_CMR_Mobile_20260520.md |
| 2026-05-22 | v2.1 → v2.2 | §2.2 — Filter Dropdown: Giá trị mặc định | "Chọn ngành nghề", "Tất cả nhu cầu", "Tất cả quy mô", "Toàn quốc" | Tất cả → `"Tất cả"` | Align CMR-03: filter dropdown mặc định "Tất cả" |
| 2026-05-22 | v2.1 → v2.2 | §2.2 — D08 behavior các filter | Tap ra ngoài → chọn lại giá trị cũ (sai format) | Tap ra ngoài khi trống → chọn lại "Tất cả" | Align CMR-03 D08 |
| 2026-05-22 | v2.1 → v2.2 | §2.2 row 6 — Nút "Áp dụng" | Chưa ghi rõ trạng thái Enabled/Disabled | Bổ sung: **Luôn Enabled** (CMR-09). Không có trạng thái Disabled. | Align CMR-09 (I06) |
| 2026-05-22 | v2.1 → v2.2 | §2.1 row 5 — Empty State | `"Empty State khi không có data (CMR-14)"` | Phân biệt: API rỗng → "Không có dữ liệu." / Search-filter → "Không tìm thấy kết quả." | Align CMR-14 |
| 2026-05-22 | v2.1 → v2.2 | §3 step 5 — Xử lý lỗi | Chỉ tham chiếu CMR-04 & CMR-07 chung | Bổ sung: First-load full-screen loading, Timeout >10s message chuẩn CMR-07, kèm nút "Thử lại" | Align CMR-07/CMR-16 |
| 2026-05-22 | v2.2 → v2.3 | §2.1 row 5 — Empty State bỏ dấu `.` | `"Không có dữ liệu."`, `"Không tìm thấy kết quả."` (có `.`) | `"Không có dữ liệu"`, `"Không tìm thấy kết quả"` (bỏ `.`) | Align CMR-14 v1.12 |
| 2026-05-22 | v2.2 → v2.3 | §2.1 row 2 — Search scope & Reset | Không mô tả search kết hợp Quick Filter, không mô tả reset | Bổ sung: Ô tìm kiếm kết hợp Quick Filter (CMR-01). Reset search/filter khi chuyển màn (CMR-01) | Align CMR-01 |
| 2026-05-22 | v2.2 → v2.3 | §2.2 — Searchable Dropdown empty | Không mô tả trường hợp không có option | Bổ sung: Khi nhập keyword không có option → hiển thị "Không có dữ liệu" (CMR-03) | Align CMR-03 |
| 2026-05-23 | v2.3 → v2.4 | §2.1 #1 — Xóa mô tả Icon thông báo | Header có "icon Thông báo (chuông). Badge dạng chấm vàng khi có thông báo mới, ẩn khi không có thông báo mới" | Xóa mô tả icon thông báo, chỉ giữ icon Quay lại | Icon thông báo là thành phần chung header, mô tả tập trung tại UC Thông báo |
