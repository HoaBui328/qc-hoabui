# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC92 — Tra cứu hồ sơ đầu tư Cá nhân; Tổ chức trên Mobile  
**Ngày tạo:** 14/05/2026  
**Tác giả:** Agent 6 (Mobile FDD Architect)  
**Phiên bản:** v1

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | han.luong & huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Khai thác thông tin xúc tiến đầu tư |
| Đối tượng thực hiện | Cá nhân / Tổ chức (Logged-in) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 14/05/2026 |
| Phiên bản | v1 |

---

## UC92 — Tra cứu hồ sơ đầu tư Cá nhân; Tổ chức trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu hồ sơ đầu tư Cá nhân; Tổ chức
- **Mô tả:** Chức năng cho phép người dùng đã đăng nhập tra cứu, tìm kiếm và xem danh sách các hồ sơ đề xuất đầu tư mà cá nhân/tổ chức đã gửi hoặc đang theo dõi trong hệ thống xúc tiến đầu tư.
- **Phân quyền:** Người dùng đã đăng nhập (Cá nhân / Tổ chức). Khách vãng lai KHÔNG truy cập được.
- **Phạm vi ngoài UC (Exclusions):** KHÔNG bao gồm: tạo mới hồ sơ đầu tư, chỉnh sửa hồ sơ, hoặc quản lý hồ sơ phía Admin.
- **Truy cập chức năng:** Sidebar → **"Xúc tiến đầu tư"** → **"Hồ sơ đầu tư"**.
- **Điều kiện tiên quyết (Preconditions):** Người dùng đã đăng nhập. Thiết bị có kết nối mạng.
- **Điều kiện kết thúc (Postconditions):** Hiển thị danh sách hồ sơ đầu tư của người dùng hoặc trạng thái rỗng.
- **Chức năng đáp ứng usecase số:** UC92 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Hồ sơ đầu tư

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về (CMR-06). |
| 2 | Tiêu đề Header | Label | "Hồ sơ đầu tư" | — | — | Font đậm, màu trắng, giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Badge + Tap → Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm hồ sơ..." | x | — | Tối đa **255 ký tự** (CMR-01). Debounce 3s. Tìm theo Mã hồ sơ, Tên dự án. Auto-trim. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Tap → Bottom Sheet (Trạng thái, Lĩnh vực, Khoảng thời gian). Active filter indicator (CMR-02). |

**Danh sách Hồ sơ (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ hồ sơ (Card) | Container | — | — | — | Lazy load 20/lần (CMR-04). Pull to Refresh (CMR-13). |
| 7 | Mã hồ sơ | Label | — | — | — | Font đậm, màu xanh dương. Format: "HS-XXXXXX". |
| 8 | Tên dự án đề xuất | Label | — | — | — | Font đậm (H2). Tối đa 2 dòng, truncate. |
| 9 | Ngày gửi | Icon + Label | — | — | — | Icon lịch + dd/MM/yyyy (CMR-12). |
| 10 | Lĩnh vực đầu tư | Icon + Label | — | — | — | Icon ngành + Tên lĩnh vực. |
| 11 | Tổng vốn đề xuất | Icon + Label | — | — | — | Icon $ + Số tiền (màu đỏ, CMR-11). |
| 12 | Trạng thái | Badge | — | — | — | CMR-05: Xanh lá = "Đã duyệt", Vàng = "Đang xử lý", Đỏ = "Từ chối", Xám = "Nháp". |
| 13 | Nút Chi tiết | Button | "Chi tiết" | — | — | Tap → Chi tiết hồ sơ. Debounce (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 14 | Nút X (Đóng) | Button (Icon) | — | — | — | CMR-02. |
| 15 | Trạng thái | Dropdown | "Tất cả" | x | — | Tất cả / Đã duyệt / Đang xử lý / Từ chối / Nháp. |
| 16 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 17 | Khoảng thời gian | Date Range | — | x | — | Lọc theo ngày gửi (CMR-15). |
| 18 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 19 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

#### 2.3 Màn hình Chi tiết Hồ sơ đầu tư

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về Danh sách (CMR-06). |
| 2 | Tiêu đề Header | Label | "Chi tiết hồ sơ" | — | — | Font đậm, màu trắng, giữa Header. |

**Khung Thông tin chi tiết:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Mã hồ sơ | Label | — | — | — | Font đậm, màu xanh dương. |
| 4 | Trạng thái | Badge | — | — | — | CMR-05. |
| 5 | Tên dự án đề xuất | Label | — | — | — | Font đậm (H1), hiển thị đầy đủ. |
| 6 | Tên nhà đầu tư | Label | — | — | — | Null → "-" (CMR-14). |
| 7 | Loại nhà đầu tư | Label | — | — | — | "Cá nhân" hoặc "Tổ chức". Null → "-" (CMR-14). |
| 8 | Lĩnh vực đầu tư | Label | — | — | — | Null → "-" (CMR-14). |
| 9 | Địa điểm đề xuất | Label | — | — | — | Null → "-" (CMR-14). |
| 10 | Tổng vốn đề xuất | Label | — | — | — | CMR-11. Null → "-" (CMR-14). |
| 11 | Ngày gửi | Label | — | — | — | dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 12 | Mô tả dự án | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 13 | Ghi chú xử lý | Label (Multiline) | — | — | — | Ghi chú từ cơ quan xử lý (nếu có). Null → "-" (CMR-14). |
| 14 | Tài liệu đính kèm | File List | — | — | — | CMR-08. Không có → Ẩn section. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách
1. API lấy danh sách hồ sơ đầu tư thuộc tài khoản đang đăng nhập.
2. Sắp xếp: ngày gửi mới nhất lên đầu.
3. Infinite Scroll (CMR-04).
4. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Realtime theo mã hồ sơ + tên dự án. Debounce 3s (CMR-01). Không tìm thấy → "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** API kèm (Status, IndustryID, DateFrom, DateTo).
3. **Kết hợp:** Tìm kiếm + Lọc đồng thời (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Tap "Chi tiết" → API chi tiết hồ sơ.
2. Loading toàn màn hình (CMR-07).
3. Null → "-" (CMR-14).

#### 3.4 Xử lý phân quyền
- Nếu người dùng chưa đăng nhập truy cập UC92 → Hệ thống chuyển về màn hình Đăng nhập (UC256) kèm toast: "Vui lòng đăng nhập để xem hồ sơ đầu tư."
- Người dùng chỉ xem được hồ sơ thuộc tài khoản của mình.

#### 3.5 Xử lý lỗi (CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng | "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + "Thử lại" | Giữ nguyên. |
| Lỗi 401 | "Phiên đăng nhập hết hạn." (Toast) | Auto refresh → redirect nếu hết hạn (CMR-07). |
| Lỗi 500 | "Hệ thống đang bận. Vui lòng thử lại sau." | Giữ nguyên. |
| Timeout (>10s) | "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + "Thử lại" | CMR-16. |

#### 3.6 Đa ngôn ngữ (CMR-17)

Text cứng dịch 5 ngôn ngữ. Nội dung API giữ nguyên bản.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Chỉ người dùng đã đăng nhập mới truy cập được. Guest → redirect Đăng nhập.
- **AC2:** Card hiển thị: Mã hồ sơ, Tên dự án, Ngày gửi, Lĩnh vực, Vốn, Trạng thái.
- **AC3:** Người dùng chỉ xem được hồ sơ của chính mình.
- **AC4:** Bộ lọc (Trạng thái, Lĩnh vực, Khoảng thời gian) hoạt động chính xác.
- **AC5:** Chi tiết hiển thị đầy đủ, null → "-".

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC92 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |
