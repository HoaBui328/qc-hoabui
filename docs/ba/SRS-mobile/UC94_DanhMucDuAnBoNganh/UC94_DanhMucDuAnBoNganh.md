# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC94 — Xem danh mục dự án đầu tư bộ ngành đang có cá nhân, tổ chức quan tâm trên Mobile  
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

## UC94 — Xem danh mục dự án đầu tư bộ ngành đang có cá nhân, tổ chức quan tâm

### 1. Mô tả chức năng

- **Tên chức năng:** Xem danh mục dự án đầu tư bộ ngành đang có cá nhân, tổ chức quan tâm
- **Mô tả:** Chức năng cho phép người dùng xem danh sách các dự án đầu tư thuộc quản lý của các Bộ/ngành mà đã có cá nhân hoặc tổ chức bày tỏ quan tâm (đăng ký quan tâm, gửi hồ sơ đề xuất). Đây là danh mục công khai giúp nhà đầu tư đánh giá mức độ cạnh tranh.
- **Phân quyền:** Toàn bộ người dùng (Khách vãng lai và người dùng đã đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** KHÔNG bao gồm: đăng ký quan tâm dự án, gửi hồ sơ đầu tư, hoặc xem danh mục dự án địa phương (UC95).
- **Truy cập chức năng:** Sidebar → **"Xúc tiến đầu tư"** → **"DA bộ ngành có NĐT quan tâm"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hiển thị danh sách dự án hoặc trạng thái rỗng.
- **Chức năng đáp ứng usecase số:** UC94 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Dự án bộ ngành có NĐT quan tâm

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về (CMR-06). |
| 2 | Tiêu đề Header | Label | "DA bộ ngành - NĐT quan tâm" | — | — | Font đậm, màu trắng, giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Badge + Tap → Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm dự án..." | x | — | Tối đa **255 ký tự** (CMR-01). Debounce 3s. Tìm theo Tên dự án. Auto-trim. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Tap → Bottom Sheet (Bộ ngành, Lĩnh vực, Quy mô vốn). Active filter indicator (CMR-02). |

**Danh sách Dự án (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ dự án (Card) | Container | — | — | — | Lazy load 20/lần (CMR-04). Pull to Refresh (CMR-13). |
| 7 | Tên dự án | Label | — | — | — | Font đậm (H2). Tối đa 2 dòng, truncate. |
| 8 | Bộ ngành quản lý | Icon + Label | — | — | — | Icon tòa nhà + Tên Bộ/ngành. |
| 9 | Lĩnh vực đầu tư | Icon + Label | — | — | — | Icon ngành + Tên lĩnh vực. |
| 10 | Tổng vốn đầu tư | Icon + Label | — | — | — | Icon $ + Số tiền (màu đỏ, CMR-11). |
| 11 | Số lượt quan tâm | Icon + Label | — | — | — | Icon người + Số lượng (VD: "12 NĐT quan tâm"). Màu xanh dương đậm. |
| 12 | Nút Chi tiết | Button | "Chi tiết" | — | — | Tap → Chi tiết dự án. Debounce (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Nút X (Đóng) | Button (Icon) | — | — | — | CMR-02. |
| 14 | Bộ ngành | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 15 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 16 | Quy mô vốn | Dropdown | "Tất cả" | x | — | Dưới 100 tỷ / 100-500 tỷ / 500 tỷ - 1.000 tỷ / Trên 1.000 tỷ. |
| 17 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 18 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

#### 2.3 Màn hình Chi tiết Dự án

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về Danh sách (CMR-06). |
| 2 | Tiêu đề Header | Label | "Chi tiết dự án" | — | — | Font đậm, màu trắng, giữa Header. |

**Khung Thông tin chi tiết:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Tên dự án | Label | — | — | — | Font đậm (H1), hiển thị đầy đủ. |
| 4 | Số lượt quan tâm | Label | — | — | — | Màu xanh dương đậm. Format: "X NĐT quan tâm". |
| 5 | Bộ ngành quản lý | Label | — | — | — | Null → "-" (CMR-14). |
| 6 | Lĩnh vực đầu tư | Label | — | — | — | Null → "-" (CMR-14). |
| 7 | Địa điểm dự án | Label | — | — | — | Null → "-" (CMR-14). |
| 8 | Tổng vốn đầu tư | Label | — | — | — | CMR-11. Null → "-" (CMR-14). |
| 9 | Quy mô dự án | Label (Multiline) | — | — | — | Mô tả quy mô. Null → "-" (CMR-14). |
| 10 | Mục tiêu dự án | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 11 | Hình thức đầu tư | Label | — | — | — | VD: "100% vốn nước ngoài", "Liên doanh". Null → "-" (CMR-14). |
| 12 | Thời gian kêu gọi | Label | — | — | — | dd/MM/yyyy - dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 13 | Tài liệu đính kèm | File List | — | — | — | CMR-08. Không có → Ẩn section. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách
1. API lấy danh sách dự án đầu tư bộ ngành có NĐT quan tâm.
2. Sắp xếp: số lượt quan tâm nhiều nhất lên đầu (mặc định).
3. Infinite Scroll (CMR-04).
4. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Realtime theo tên dự án. Debounce 3s (CMR-01). Không tìm thấy → "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** API kèm (MinistryID, IndustryID, CapitalRange).
3. **Kết hợp:** Tìm kiếm + Lọc đồng thời (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Tap "Chi tiết" → API chi tiết dự án.
2. Loading toàn màn hình (CMR-07).
3. Null → "-" (CMR-14).

#### 3.4 Xử lý lỗi (CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng | "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + "Thử lại" | Giữ nguyên. |
| Lỗi 401 | "Phiên đăng nhập hết hạn." (Toast) | Auto refresh → redirect nếu hết hạn (CMR-07). |
| Lỗi 500 | "Hệ thống đang bận. Vui lòng thử lại sau." | Giữ nguyên. |
| Timeout (>10s) | "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + "Thử lại" | CMR-16. |

#### 3.5 Đa ngôn ngữ (CMR-17)

Text cứng dịch 5 ngôn ngữ. Nội dung API giữ nguyên bản.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Card hiển thị: Tên DA, Bộ ngành, Lĩnh vực, Vốn, Số lượt quan tâm.
- **AC2:** Số lượt quan tâm hiển thị nổi bật (màu xanh dương đậm).
- **AC3:** Sắp xếp mặc định theo số lượt quan tâm giảm dần.
- **AC4:** Bộ lọc 3 tiêu chí (Bộ ngành, Lĩnh vực, Quy mô vốn).
- **AC5:** Chi tiết hiển thị đầy đủ, null → "-".

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC94 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |
