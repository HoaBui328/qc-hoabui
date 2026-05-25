# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC88 — Tra cứu chương trình xúc tiến đầu tư Quốc gia trên Mobile  
**Ngày tạo:** 14/05/2026  
**Tác giả:** Agent 6 (Mobile FDD Architect)  
**Phiên bản:** v1

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | han.luong & huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Khai thác thông tin xúc tiến đầu tư |
| Đối tượng thực hiện | Cá nhân / Tổ chức (Guest & Logged-in) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 14/05/2026 |
| Phiên bản | v1 |

---

## UC88 — Tra cứu chương trình xúc tiến đầu tư Quốc gia trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu chương trình xúc tiến đầu tư Quốc gia
- **Mô tả:** Chức năng cho phép người dùng tra cứu, tìm kiếm và xem danh sách các chương trình xúc tiến đầu tư cấp Quốc gia theo nhiều tiêu chí như năm, lĩnh vực, trạng thái thực hiện.
- **Phân quyền:** Toàn bộ người dùng (Khách vãng lai và người dùng đã đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** UC này KHÔNG bao gồm: tra cứu chương trình XTĐT Bộ ngành (UC89), tra cứu chương trình XTĐT Địa phương (UC90), hoặc các nghiệp vụ quản lý chương trình phía Admin.
- **Truy cập chức năng:** Sidebar → Mục **"Xúc tiến đầu tư"** → Chọn **"Chương trình XTĐT Quốc gia"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định (Wifi/4G/5G).
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị danh sách các chương trình XTĐT Quốc gia thỏa mãn điều kiện hoặc hiển thị trạng thái rỗng nếu không có dữ liệu.
- **Chức năng đáp ứng usecase số:** UC88 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Chương trình XTĐT Quốc gia

**Mô tả giao diện:**
Màn hình danh sách chương trình với khung Header màu đỏ đậm đặc trưng. Bên dưới là thanh công cụ bao gồm Ô tìm kiếm và Nút lọc. Phần thân màn hình hiển thị danh sách các thẻ Chương trình (Card) cuộn dọc, mỗi thẻ chứa thông tin tóm tắt và nút điều hướng chi tiết.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về màn hình trước đó. (Xem CMR-06). |
| 2 | Tiêu đề Header | Label | "CT XTĐT Quốc gia" | — | — | Font đậm, màu trắng, nằm giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Icon chuông trắng, có Badge đỏ nhỏ ở góc trên phải khi có thông báo mới. Tap → Mở màn hình Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm nhanh theo tên chương trình" | x | — | Nền xám nhạt, icon kính lúp bên trái. Tối đa **255 ký tự** (CMR-01). Nhập từ khóa → Tìm kiếm theo Tên chương trình. Debounce 3 giây (CMR-01). Auto-trim whitespace đầu/cuối. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Nằm bên phải ô tìm kiếm. Tap → Mở Modal Bottom Sheet bộ lọc (Năm, Lĩnh vực, Trạng thái). Có active filter indicator (CMR-02). |

**Danh sách Chương trình (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ chương trình (Card) | Container | — | — | — | Khung trắng, bo góc, shadow nhẹ. Lazy load 20 bản ghi/lần (CMR-04). Hỗ trợ Pull to Refresh (CMR-13). |
| 7 | Tên chương trình | Label | — | — | — | Font đậm (H2), màu đen. Tối đa 2 dòng, quá 2 dòng hiển thị `...` (truncate). |
| 8 | Năm thực hiện | Icon + Label | — | — | — | Icon lịch + Năm (VD: "2026"). |
| 9 | Lĩnh vực | Icon + Label | — | — | — | Icon ngành + Tên lĩnh vực (VD: "Công nghệ cao", "Nông nghiệp"). |
| 10 | Cơ quan chủ trì | Icon + Label | — | — | — | Icon tòa nhà + Tên cơ quan (VD: "Bộ Kế hoạch và Đầu tư"). |
| 11 | Trạng thái | Badge | — | — | — | Badge trạng thái theo CMR-05: Xanh lá = "Đang thực hiện", Vàng = "Chưa triển khai", Xám = "Đã kết thúc". |
| 12 | Nút Chi tiết | Button | "Chi tiết" | — | — | Button viền xám, full-width cuối Card. Tap → Điều hướng đến Màn hình Chi tiết chương trình. Debounce Navigation (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Nút X (Đóng) | Button (Icon) | — | — | — | Góc phải trên cùng. Tap → Đóng Bottom Sheet, không thay đổi kết quả (CMR-02). |
| 14 | Năm | Dropdown | "Tất cả" | x | — | Danh sách năm từ API danh mục. Searchable dropdown (CMR-03). |
| 15 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Danh sách lĩnh vực đầu tư từ API danh mục. Searchable dropdown (CMR-03). |
| 16 | Trạng thái | Dropdown | "Tất cả" | x | — | Giá trị: Tất cả / Đang thực hiện / Chưa triển khai / Đã kết thúc. |
| 17 | Nút "Áp dụng" | Button (Primary) | — | — | — | Tap → Đóng bộ lọc, tải lại danh sách với tiêu chí đã chọn (CMR-02). |
| 18 | Nút "Đặt lại" | Button (Secondary) | — | — | — | Tap → Reset tất cả trường về giá trị mặc định (CMR-02). |

#### 2.3 Màn hình Chi tiết Chương trình XTĐT Quốc gia

**Mô tả giao diện:**
Màn hình chi tiết hiển thị toàn bộ thông tin của một chương trình XTĐT Quốc gia. Header đỏ đậm với nút quay lại và tiêu đề. Phần thân cuộn dọc hiển thị các nhóm thông tin.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về màn hình Danh sách (CMR-06). |
| 2 | Tiêu đề Header | Label | "Chi tiết chương trình" | — | — | Font đậm, màu trắng, nằm giữa Header. |

**Khung Thông tin chi tiết:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Tên chương trình | Label | — | — | — | Font đậm (H1), màu đen. Hiển thị đầy đủ, không truncate. |
| 4 | Trạng thái | Badge | — | — | — | Badge trạng thái theo CMR-05. |
| 5 | Năm thực hiện | Label | — | — | — | Format: "Năm [YYYY]" (VD: "Năm 2026"). |
| 6 | Cơ quan chủ trì | Label | — | — | — | Tên cơ quan chủ trì chương trình. Giá trị null → hiển thị "-" (CMR-14). |
| 7 | Lĩnh vực đầu tư | Label | — | — | — | Tên lĩnh vực. Giá trị null → hiển thị "-" (CMR-14). |
| 8 | Mục tiêu chương trình | Label (Multiline) | — | — | — | Mô tả mục tiêu. Giá trị null → hiển thị "-" (CMR-14). |
| 9 | Nội dung hoạt động | Label (Multiline) | — | — | — | Mô tả các hoạt động chính. Giá trị null → hiển thị "-" (CMR-14). |
| 10 | Kinh phí dự kiến | Label | — | — | — | Định dạng theo CMR-11. Đơn vị: VNĐ. Giá trị null → hiển thị "-" (CMR-14). |
| 11 | Thời gian thực hiện | Label | — | — | — | Format: "dd/MM/yyyy - dd/MM/yyyy" (CMR-12). Giá trị null → hiển thị "-" (CMR-14). |
| 12 | Địa điểm thực hiện | Label | — | — | — | Tên địa điểm/quốc gia. Giá trị null → hiển thị "-" (CMR-14). |
| 13 | Tài liệu đính kèm | File List | — | — | — | Danh sách file đính kèm (nếu có). Tap → Xem/Tải theo CMR-08. Không có file → Ẩn section này. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách chương trình
1. Hệ thống gọi API lấy danh sách các chương trình XTĐT Quốc gia.
2. Mặc định sắp xếp theo năm thực hiện mới nhất lên đầu, trong cùng năm sắp xếp theo ngày tạo mới nhất.
3. Khi người dùng cuộn tới cuối trang, hệ thống tự động tải thêm dữ liệu (Infinite Scroll) theo CMR-04.
4. Trường hợp không có dữ liệu: Hiển thị "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Lọc dữ liệu realtime theo từ khóa (tên chương trình). Debounce 3 giây (CMR-01). Nếu không tìm thấy → Hiển thị "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** Khi áp dụng bộ lọc, hệ thống gửi API kèm tham số (Year, IndustryID, Status) để làm mới danh sách.
3. **Kết hợp:** Tìm kiếm + Lọc áp dụng đồng thời, kết quả phải thỏa cả hai điều kiện (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Người dùng tap nút "Chi tiết" trên Card → Hệ thống gọi API lấy thông tin chi tiết chương trình.
2. Hiển thị loading state toàn màn hình trong khi chờ API (CMR-07).
3. Sau khi nhận dữ liệu → Hiển thị toàn bộ thông tin chi tiết.
4. Các trường có giá trị null → Hiển thị "-" (CMR-14).

#### 3.4 Xử lý lỗi (Tham chiếu CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng / Mất kết nối | "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + nút "Thử lại" | Giữ nguyên màn hình, hiển thị nút Thử lại. |
| Lỗi 401 (Session hết hạn) | "Phiên đăng nhập hết hạn." (Toast) | Auto refresh token. Nếu refresh token hết hạn (>15 ngày) → chuyển về Đăng nhập (CMR-07). |
| Lỗi API (HTTP 500) | "Hệ thống đang bận. Vui lòng thử lại sau." | Giữ nguyên màn hình, hiển thị thông báo. |
| Timeout (>10 giây) | "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + nút "Thử lại" | Hiển thị thông báo, giữ nguyên màn hình (CMR-16). |

#### 3.5 Đa ngôn ngữ (→ CMR-17)

Toàn bộ text cứng trên màn hình UC88 (header, placeholder, label bộ lọc, thông báo lỗi, empty state) được dịch sang ngôn ngữ hiển thị tương ứng. Hỗ trợ 5 ngôn ngữ: VI, EN, ZH, JA, KO. Nội dung dữ liệu từ API hiển thị nguyên bản.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Danh sách chương trình hiển thị đầy đủ: Tên, Năm, Lĩnh vực, Cơ quan chủ trì, Trạng thái.
- **AC2:** Badge trạng thái hiển thị đúng màu theo CMR-05.
- **AC3:** Bộ lọc hoạt động chính xác với 3 tiêu chí (Năm, Lĩnh vực, Trạng thái).
- **AC4:** Tìm kiếm debounce 3 giây, không gây giật lag giao diện.
- **AC5:** Màn hình chi tiết hiển thị đầy đủ thông tin, các trường null hiển thị "-".
- **AC6:** Tài liệu đính kèm mở/tải đúng theo CMR-08.

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC88 theo format UC90 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |

