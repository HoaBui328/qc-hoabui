# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile  
**Ngày tạo:** 20/05/2026  
**Tác giả:** Agent 6 (Mobile FDD Architect)  
**Phiên bản:** v2.3

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | han.luong & huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Khai thác thông tin xúc tiến đầu tư |
| Đối tượng thực hiện | Cá nhân / Tổ chức (Logged-in) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 20/05/2026 |
| Phiên bản | v2.3 |

---

## UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu dự án kêu gọi đầu tư trên Mobile
- **Mô tả:** Chức năng cho phép nhà đầu tư (cá nhân/tổ chức) bổ sung thông tin nhu cầu đầu tư, nhận gợi ý dự án phù hợp thông qua matching tự động, tra cứu danh sách dự án kêu gọi đầu tư, và đăng ký quan tâm dự án.
- **Phân quyền:** Người dùng đã đăng nhập (Cá nhân / Tổ chức). Khách vãng lai KHÔNG truy cập được. Cá nhân và Tổ chức có cùng giao diện và chức năng, không phân biệt. Trường hợp Token chứa vai trò (role) không hợp lệ (ngoài 3 role trên) → Hệ thống xử lý như lỗi session hết hạn 401 theo quy định CMR-07 (không cho phép truy cập).
- **Phạm vi ngoài UC (Exclusions):** UC87 KHÔNG bao gồm: NĐT tự đề xuất dự án (thuộc phân hệ XTĐT), quản lý/phê duyệt dự án phía Admin, tra cứu CT XTĐT Quốc gia (UC88), tra cứu văn bản MOU (UC91).
- **Truy cập chức năng:** Sidebar → Mục **"Xúc tiến đầu tư"** → Chọn **"Dự án kêu gọi đầu tư"**
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định, người dùng đã đăng nhập vào hệ thống.
- **Điều kiện kết thúc (Postconditions):** 
  - (a) Sau khi bổ sung thông tin → Thông tin nhu cầu đầu tư của NĐT được lưu trên hệ thống, kết quả matching realtime trả về danh sách đề xuất phù hợp.
  - (b) Sau khi đăng ký quan tâm → Trạng thái đăng ký được lưu trên server, nút chuyển đổi thành "Hủy quan tâm" và đồng bộ trạng thái giữa màn hình Danh sách & Chi tiết.
  - (c) Sau khi hủy quan tâm → Trạng thái đăng ký bị xóa khỏi hệ thống, nút chuyển đổi lại thành "Đăng ký quan tâm".
- **Chức năng đáp ứng usecase số:** UC87 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình chính — Hub Dự án kêu gọi đầu tư (Tham chiếu: UC87 - Onboard.png)

**Mô tả giao diện:**
Header đỏ đậm "Dự án kêu gọi đầu tư" với nút Quay lại. Phần thân gồm 2 khối chức năng chính dạng Card lớn, xếp dọc: (1) Bổ sung thông tin NĐT - Gợi ý dự án phù hợp, (2) Danh sách dự án đề xuất.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về màn hình trước. (Xem CMR-06) |
| 2 | Tiêu đề Header | Label | "Dự án kêu gọi đầu tư" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, nằm giữa header, nền đỏ đậm. |
| 3 | Card "Bổ sung thông tin NĐT" | Card (Navigation) | — | — | — | **Quy tắc hiển thị:**<br>- Nền trắng, bo góc, shadow nhẹ. Icon minh họa + Tiêu đề "Bổ sung thông tin nhà đầu tư - Gợi ý dự án phù hợp" + Mô tả ngắn.<br>- Nút **"Cập nhật"** nằm trong card.<br>**Quy tắc hành động:**<br>- Tap card hoặc tap nút "Cập nhật" → Điều hướng đến Màn hình 2.2 (Bổ sung thông tin NĐT).<br>- Debounce Navigation (CMR-18). |
| 4 | Card "Danh sách dự án đề xuất" | Card (Navigation) | — | — | — | **Quy tắc hiển thị:**<br>- Nền trắng, bo góc, shadow nhẹ. Icon danh sách + Tiêu đề "Danh sách dự án đề xuất cho nhà đầu tư" + Mô tả ngắn.<br>- Nút **"Xem danh sách"** nằm trong card.<br>**Quy tắc hành động:**<br>- Tap card hoặc tap nút "Xem danh sách" → Điều hướng đến Màn hình 2.3 (Danh sách dự án đề xuất).<br>- Debounce Navigation (CMR-18). |

---
#### 2.2 Màn hình Bổ sung thông tin NĐT — Gợi ý dự án phù hợp (Tham chiếu: UC87 - Bổ sung thông tin.png)

**Mô tả giao diện:**
Màn hình form cho phép NĐT bổ sung nhu cầu đầu tư và thông tin quan tâm. Nếu NĐT đã bổ sung trước đó, form hiển thị thông tin đã điền (cho phép sửa). Sau khi bổ sung đầy đủ, NĐT nhấn "Xem dự án phù hợp" → hệ thống matching tự động (realtime) → hiển thị danh sách dự án phù hợp.

**Trạng thái mặc định (NĐT mở form lần đầu — chưa từng bổ sung thông tin):**
- Trường bắt buộc "Lĩnh vực quan tâm": Giá trị mặc định "Tất cả".
- Trường bắt buộc "Địa bàn mong muốn": Giá trị mặc định "Tất cả".
- Các Dropdown không bắt buộc (Ngành kinh tế, Hình thức đầu tư, Quốc gia hợp tác): Giá trị mặc định "Tất cả".
- Textbox (Quy mô vốn): Để trống, hiển thị placeholder.
- Textarea (Mô tả nhu cầu đầu tư): Để trống, hiển thị placeholder.
- Nút "Xem dự án phù hợp": **Luôn Enabled** (CMR-09). Tap → validate toàn bộ form, hiển thị inline error nếu thiếu trường bắt buộc.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về Hub (2.1). (CMR-06) |
| 2 | Tiêu đề Header | Label | "Bổ sung thông tin" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, giữa header. |


**Quy tắc trường bắt buộc (CMR-09):** Tất cả trường bắt buộc (cột "Bắt buộc" = x) hiển thị dấu (*) màu đỏ bên cạnh label. VD: "Lĩnh vực quan tâm *", "Địa bàn mong muốn *".

**Khung Form bổ sung thông tin:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Lĩnh vực quan tâm | Dropdown (Multi-select) | "Tất cả" | x | x | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả".<br>- Cho phép chọn nhiều lĩnh vực, không giới hạn số lượng. Danh sách từ API danh mục. Searchable (CMR-03).<br>- Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03).<br>- Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa.<br>- Option đã chọn sẽ bị ẩn (remove) khỏi danh sách dropdown. Khi user xóa chip (tap X) → option tương ứng quay lại danh sách dropdown.<br>- **Lưu ý:** Trường luôn có giá trị (fallback "Tất cả" khi rỗng), không xảy ra trạng thái bỏ trống → không cần inline error. |
| 4 | Ngành kinh tế | Dropdown (Multi-select) | "Tất cả" | x | — | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả". Searchable (CMR-03).<br>- Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03).<br>- Không giới hạn số lượng. Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa.<br>- Option đã chọn sẽ bị ẩn (remove) khỏi danh sách dropdown. Khi user xóa chip (tap X) → option tương ứng quay lại danh sách dropdown. |
| 5 | Địa bàn mong muốn | Dropdown (Multi-select) | "Tất cả" | x | x | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả". Danh sách 63 tỉnh/TP. Searchable (CMR-03).<br>- Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03).<br>- Không giới hạn số lượng. Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa.<br>- Option đã chọn sẽ bị ẩn (remove) khỏi danh sách dropdown. Khi user xóa chip (tap X) → option tương ứng quay lại danh sách dropdown.<br>- **Lưu ý:** Trường luôn có giá trị (fallback "Tất cả" khi rỗng), không xảy ra trạng thái bỏ trống → không cần inline error. |
| 6 | Hình thức đầu tư | Dropdown | "Tất cả" | x | — | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả".<br>- Giá trị: Tất cả / 100% vốn nước ngoài / Liên doanh / Hợp đồng BCC / Khác.<br>- Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03). |
| 7 | Quy mô vốn dự kiến | Textbox (Number) | — | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Nhập quy mô vốn dự kiến".<br>- Chỉ nhập số nguyên dương > 0 (không chấp nhận số âm, số 0 hay ký tự đặc biệt). Đơn vị: tỷ VNĐ (cố định, hiển thị label bên phải textbox).<br>- Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11).<br>- Tối đa 255 ký tự.<br>- Message lỗi validation nếu nhập <= 0: "Quy mô vốn dự kiến phải lớn hơn 0" (CMR-11).<br>- Message lỗi Max length: *"Quy mô vốn dự kiến không được vượt quá 255 ký tự!"* (CMR-09). |
| 8 | Quốc gia mong muốn hợp tác | Dropdown (Multi-select) | "Tất cả" | x | — | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả". Danh sách quốc gia từ API. Searchable (CMR-03).<br>- Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03).<br>- Không giới hạn số lượng. Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa.<br>- Option đã chọn sẽ bị ẩn (remove) khỏi danh sách dropdown. Khi user xóa chip (tap X) → option tương ứng quay lại danh sách dropdown. |
| 9 | Mô tả nhu cầu đầu tư | Textarea | — | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Nhập mô tả nhu cầu đầu tư".<br>- Tối đa 3000 ký tự. Auto-trim whitespace khi out-click (CMR-09).<br>- Message lỗi Max length: *"Mô tả nhu cầu đầu tư không được vượt quá 3000 ký tự!"* (CMR-09). |
| 10 | Nút "Xem dự án phù hợp" | Button (Primary) | — | — | — | **Quy tắc hiển thị:**<br>- Luôn Enabled (CMR-09). Tap → validate toàn bộ form.<br>**Quy tắc hành động:**<br>- Tap → Hệ thống lưu thông tin NĐT + gọi API matching → Hiển thị kết quả matching (danh sách dự án phù hợp) tại Màn hình 2.3. |

---

#### 2.3 Màn hình Danh sách dự án đề xuất cho nhà đầu tư (Tham chiếu: UC87 - Dự án đề xuất.png, UC87 - Dự án đề xuất - Huỷ quan tâm.png, UC87 - Chưa có gợi ý.png, UC87 - Dự án đề xuất - Empty state.png)

**Mô tả giao diện:**
Màn hình danh sách các dự án phù hợp (matching tự động + gán thủ công bởi cơ quan quản lý). Có thanh tìm kiếm + bộ lọc nâng cao. NĐT có thể đăng ký quan tâm dự án từ danh sách.

**Trạng thái đặc biệt — NĐT chưa bổ sung thông tin (Tham chiếu: UC87 - Chưa có gợi ý.png):**
Nếu NĐT chưa từng bổ sung thông tin nhu cầu đầu tư (chưa thực hiện Chức năng 1), màn hình hiển thị:
- Tiêu đề: **"Chưa có gợi ý dự án"**
- Mô tả: *"Vui lòng bổ sung thông tin nhu cầu đầu tư để hệ thống gợi ý các dự án phù hợp nhất với bạn."*
- Nút **"Bổ sung ngay +"** (nền đỏ đậm, text trắng, icon "+"):
  - Tap → Điều hướng đến Màn hình 2.2 (Bổ sung thông tin NĐT).
  - Debounce Navigation (CMR-18).

**Trạng thái đặc biệt — Danh sách rỗng:**
- **No data (không có dữ liệu):** Khi hệ thống chưa có dự án kêu gọi đầu tư nào (API trả về danh sách rỗng ngay từ đầu dù user đã sử dụng filter/search) → Hiển thị hình ảnh trống + thông báo: *"Không có dữ liệu."* (Tham chiếu: UC87 - Dự án đề xuất - Empty state.png, CMR-14).
- **No result (không tìm thấy kết quả):** Khi người dùng tìm kiếm/lọc hoặc matching không trả về kết quả phù hợp → Hiển thị hình ảnh trống + thông báo: *"Không tìm thấy kết quả."* (CMR-14).

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về Hub (2.1). (CMR-06) |
| 2 | Tiêu đề Header | Label | "Dự án đề xuất" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, giữa header. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Ô tìm kiếm | Textbox (Search) | — | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Tìm kiếm nhanh theo tên dự án". Icon kính lúp bên trái. Tối đa 255 ký tự (CMR-01).<br>**Quy tắc hành động:**<br>- Debounce 3 giây (CMR-01). Tìm theo Tên dự án.<br>- Auto-trim whitespace (CMR-01). |
| 4 | Nút Lọc | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Mở Bottom Sheet bộ lọc nâng cao.<br>- Active filter indicator (CMR-02). |

**State Persistence (CMR-01):** Khi NĐT tap vào card dự án để xem chi tiết (§2.4), sau đó nhấn Quay lại → Hệ thống giữ nguyên trạng thái tìm kiếm và bộ lọc đã áp dụng trước đó (từ khoá tìm kiếm, giá trị bộ lọc, vị trí scroll). Không reset về trạng thái mặc định.

**Danh sách Dự án (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 5 | Thẻ dự án (Card) | Container | — | — | — | **Quy tắc hiển thị:**<br>- Khung trắng, bo góc, shadow nhẹ. Lazy load 20 bản ghi/lần (CMR-04).<br>- Hỗ trợ Pull to Refresh (CMR-13).<br>**Quy tắc hành động:**<br>- Tap card → Điều hướng đến Màn hình 2.4 (Chi tiết dự án). Debounce Navigation (CMR-18). |
| 6 | Tên dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm (H2), màu đen. Tối đa 2 dòng, truncate `...`. |
| 7 | Lĩnh vực | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon ngành + Tên lĩnh vực. Font nhỏ, màu xám. |
| 8 | Địa bàn | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon định vị + Tên tỉnh/TP hoặc KCN. Font nhỏ, màu xám. |
| 9 | Tổng vốn đầu tư dự kiến | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon tiền (₫) + tiền tố "Vốn: " (màu xám) + Số tiền (màu đỏ) + đơn vị "tỷ VNĐ" (màu đỏ). Font nhỏ. VD: `⊙ Vốn: 8.200 tỷ VNĐ`. Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11). |
| 10 | Ngày đăng ký | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon lịch (📅) + tiền tố "Đăng ký: " + dd/MM/yyyy (CMR-12). VD: `📅 Đăng ký: 12/05/2026`. Font nhỏ, màu xám. |
| 11 | Nút "Đăng ký quan tâm" / "Hủy quan tâm" | Button (Primary/Secondary, Small) | — | — | — | **Quy tắc hiển thị:**<br>- Trạng thái mặc định: "Đăng ký quan tâm" (nền đỏ, text trắng).<br>- Sau khi đăng ký thành công: Đổi thành "Hủy quan tâm" (nền trắng, viền xám, text xám). (Tham chiếu: UC87 - Dự án đề xuất - Huỷ quan tâm.png)<br>- **Loading state:** Khi đang chờ API → button disabled + hiển thị spinner cục bộ thay text (CMR-07). Sau khi API trả về → khôi phục trạng thái tương ứng.<br>**Quy tắc hành động:**<br>- Tap "Đăng ký quan tâm" → API đăng ký → Toast "Đăng ký quan tâm thành công." → Đổi trạng thái nút.<br>- Tap "Hủy quan tâm" → API hủy → Toast "Đã hủy đăng ký quan tâm." → Đổi lại trạng thái nút.<br>- Không giới hạn số dự án đăng ký quan tâm.<br>- Debounce (CMR-18). |

**Modal Bottom Sheet — Bộ lọc nâng cao (Tham chiếu: UC87 - Filter dự án.png):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 12 | Nút X (Đóng) | Button (Icon) | — | — | — | Đóng Bottom Sheet, không thay đổi kết quả (CMR-02). |
| 13 | Loại dự án | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Tất cả / Trong nước / Nước ngoài / Trong & ngoài nước. Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03). |
| 14 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Searchable (CMR-03). Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03). Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03). |
| 15 | Ngành kinh tế | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Searchable (CMR-03). Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03). Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03). |
| 16 | Địa bàn (Tỉnh/TP) | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". 63 tỉnh/TP. Searchable (CMR-03). Xóa hết keyword → hiển thị lại placeholder. Tap ra ngoài khi rỗng → chọn lại "Tất cả" (CMR-03). Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03). |
| 17 | Hình thức đầu tư | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Tất cả / 100% vốn nước ngoài / Liên doanh / Hợp đồng BCC / Khác. Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03). |
| 18 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 19 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

---

#### 2.4 Màn hình Chi tiết Dự án kêu gọi đầu tư (Tham chiếu: UC87 - Chi tiết dự án.png)

**Mô tả giao diện:**
Màn hình cuộn dọc hiển thị toàn bộ thông tin chi tiết của một dự án kêu gọi đầu tư, chia thành các section theo nhóm thông tin.

**Quy tắc chung hiển thị các Section:**
- Các Section từ 1 đến 6 luôn luôn hiển thị trên giao diện.
- Tất cả trường thông tin trong §2.4 là **read-only** (chỉ đọc), không cho phép chỉnh sửa.
- Đối với trường thông tin không có dữ liệu (null), hiển thị dấu gạch ngang "-" (CMR-14).
- Đối với trường thông tin có nội dung dài (Tên dự án, Mục tiêu dự án, Tình trạng hiện tại...): hiển thị đầy đủ, tự động xuống dòng (text wrap). Không cắt ngắn (truncate).
- Riêng Section 7 (Tài liệu đính kèm) sẽ ẩn toàn bộ Section nếu không có tệp đính kèm nào.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về Danh sách (2.3). (CMR-06) |
| 2 | Tiêu đề Header | Label | "Chi tiết dự án" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, giữa header. |

---


**Section 1 — Thông tin chung:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Tiêu đề section | Label | "1. Thông tin chung" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 4 | Tên dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm (H1), hiển thị đầy đủ, tự động xuống dòng. |
| 5 | Mã dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Null → `-` (CMR-14). |
| 6 | Lĩnh vực | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |
| 7 | Ngành kinh tế | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |
| 8 | Loại dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |
| 9 | Địa bàn | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Hiển thị đầy đủ, tự động xuống dòng (có thể bao gồm Huyện + Tỉnh/TP). Null → `-` (CMR-14). |
| 10 | Hình thức đầu tư | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Null → `-` (CMR-14). |

---

**Section 2 — Cơ quan quản lý dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 11 | Tiêu đề section | Label | "2. Cơ quan quản lý dự án" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 12 | Cơ quan chủ quản | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |
| 13 | Đơn vị triển khai | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |

---

**Section 3 — Thông tin liên hệ:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 14 | Tiêu đề section | Label | "3. Thông tin liên hệ" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 15 | Người liên hệ | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Null → `-` (CMR-14). |
| 16 | Chức vụ | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font thường. Null → `-` (CMR-14). |
| 17 | Email | Label | — | — | — | **Quy tắc hiển thị:**<br>- Read-only, hiển thị dạng text thuần (không phải link tappable). Null → `-` (CMR-14). |
| 18 | Điện thoại | Label | — | — | — | **Quy tắc hiển thị:**<br>- Read-only, hiển thị dạng text thuần (không phải link tappable). Null → `-` (CMR-14). |

---

**Section 4 — Mục tiêu, quy mô dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 19 | Tiêu đề section | Label | "4. Mục tiêu, quy mô dự án" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 20 | Mục tiêu dự án | Label (Multiline) | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |
| 21 | Quy mô diện tích | Label | — | — | — | **Quy tắc hiển thị:**<br>- Đơn vị: hecta hoặc m². Null → `-` (CMR-14). |
| 22 | Công suất | Label (Multiline) | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |

---


**Section 5 — Nguồn vốn dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 23 | Tiêu đề section | Label | "5. Nguồn vốn dự án" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 24 | Tổng vốn đầu tư | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ, cỡ lớn. Đơn vị: tỷ VNĐ. VD: `12.500 tỷ VNĐ`. Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11). Null → `-` (CMR-14). |
| 25 | Vốn nhà nước | Label | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị trong khung bo góc. Số tiền kèm tỷ lệ phần trăm (%). VD: "4.000 tỷ VND (32%)". CMR-11. Null → `-` (CMR-14). |
| 26 | Vốn tư nhân/FDI | Label | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị trong khung bo góc (bên cạnh Vốn nhà nước). Số tiền kèm tỷ lệ phần trăm (%). VD: "8.500 tỷ VND (68%)". CMR-11. Null → `-` (CMR-14). |

---

**Section 6 — Tiến độ dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 27 | Tiêu đề section | Label | "6. Tiến độ dự án" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 28 | Thời gian bắt đầu | Label | — | — | — | **Quy tắc hiển thị:**<br>- Format: Quý/Năm (VD: "Quý 2/2026"). Null → `-` (CMR-14). |
| 29 | Thời gian hoàn thành | Label | — | — | — | **Quy tắc hiển thị:**<br>- Format: Quý/Năm (VD: "Quý 4/2029"). Null → `-` (CMR-14). |
| 30 | Tình trạng hiện tại | Badge + Label | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị badge trạng thái (icon + nền màu) + mô tả chi tiết. Hiển thị đầy đủ, tự động xuống dòng. Null → `-` (CMR-14). |

---

**Section 7 — Tài liệu đính kèm:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 31 | Tiêu đề section | Label | "7. Tài liệu đính kèm" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ đậm, căn trái. |
| 32 | Danh sách tài liệu | List (File Item) | — | — | — | **Quy tắc hiển thị:**<br>- Mỗi item: Icon loại file (📄) + Tên tài liệu. Không có nút "Tải xuống" riêng.<br>**Quy tắc hành động:**<br>- Tap vào item tài liệu → Xem/Tải theo CMR-08.<br>- **Trạng thái Empty:** Nếu không có tài liệu → Ẩn toàn bộ section. |

---

**Nút CTA cuối màn hình:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 31 | Nút "Đăng ký quan tâm" / "Hủy quan tâm" | Button (Primary/Secondary, Full-width) | — | — | — | **Quy tắc hiển thị:**<br>- Sticky bottom.<br>- Trạng thái mặc định: "Đăng ký quan tâm" (nền đỏ, text trắng).<br>- Nếu NĐT đã đăng ký: "Hủy quan tâm" (nền trắng, viền xám, text xám).<br>- **Loading state:** Khi đang chờ API → button disabled + hiển thị spinner cục bộ thay text (CMR-07). Sau khi API trả về → khôi phục trạng thái tương ứng.<br>**Quy tắc hành động:**<br>- Tap "Đăng ký quan tâm" → API đăng ký → Toast "Đăng ký quan tâm thành công." → Đổi trạng thái.<br>- Tap "Hủy quan tâm" → API hủy → Toast "Đã hủy đăng ký quan tâm." → Đổi lại trạng thái. |

---


### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng bổ sung thông tin NĐT & Matching

1. NĐT vào Hub (2.1) → Tap "Bổ sung thông tin NĐT".
2. Hệ thống hiển thị form bổ sung (2.2). Nếu NĐT đã điền trước đó → form pre-fill dữ liệu cũ, cho phép sửa.
3. NĐT điền/sửa thông tin nhu cầu đầu tư → Nhấn "Xem dự án phù hợp".
4. Hệ thống gọi API matching (realtime). Loading toàn màn hình (CMR-07).
5. **Thuật toán matching (Hybrid):**
   - Form bắt buộc NĐT điền cả Lĩnh vực và Địa bàn. Khi matching, dự án chỉ cần khớp **ít nhất 1 trong 2 tiêu chí** (Lĩnh vực HOẶC Địa bàn) để được đưa vào kết quả.
   - Bonus: các tiêu chí còn lại (Ngành kinh tế, Hình thức đầu tư, Quốc gia) tăng thứ tự ưu tiên.
   - Đối với **Quy mô vốn**: Dự án được cộng điểm ưu tiên nếu Vốn đầu tư của dự án nằm trong khoảng **+/- 20%** so với số vốn NĐT nhập.
   - Sắp xếp: mức độ phù hợp giảm dần (score không hiển thị cho NĐT).
6. API trả về kết quả → Điều hướng đến Màn hình 2.3 với danh sách matching mới (**thay thế hoàn toàn** danh sách cũ nếu có).
7. Nếu không có dự án phù hợp → Hiển thị "Không tìm thấy kết quả." (CMR-14).

#### 3.2 Luồng tra cứu danh sách dự án đề xuất

1. NĐT vào Hub (2.1) → Tap "Danh sách dự án đề xuất" → Màn hình 2.3.
2. Nếu NĐT **chưa từng bổ sung thông tin** → Hiển thị empty state "Chưa có gợi ý dự án" + mô tả + nút "Bổ sung ngay +".
3. Nếu NĐT đã bổ sung → Hệ thống gọi API lấy danh sách dự án đề xuất (matching + gán thủ công).
4. Nguồn dữ liệu: Danh sách dự án kêu gọi NĐT trong nước + nước ngoài + trong & ngoài nước.
5. Sắp xếp mặc định: mức độ phù hợp giảm dần.
6. Infinite Scroll (CMR-04).
7. Không có dữ liệu → "Không có dữ liệu." (CMR-14). Tìm kiếm/lọc không có kết quả → "Không tìm thấy kết quả." (CMR-14).

#### 3.3 Luồng đăng ký / hủy đăng ký quan tâm dự án

1. NĐT tap "Đăng ký quan tâm" trên Card hoặc trong Chi tiết.
2. Hệ thống gọi API đăng ký quan tâm.
3. Tap nút "Đăng ký quan tâm" / "Hủy quan tâm" sẽ kích hoạt cơ chế loading trên button (disabled + spinner cục bộ theo CMR-07), đồng thời áp dụng cơ chế Debounce (CMR-18) chỉ nhận action đầu tiên cho đến khi có phản hồi API.
4. Thành công → Toast "Đăng ký quan tâm thành công." → Nút đổi thành "Hủy quan tâm".
5. NĐT tap "Hủy quan tâm" → Hệ thống gọi API hủy → Toast "Đã hủy đăng ký quan tâm." → Nút đổi lại "Đăng ký quan tâm".
6. Không giới hạn số dự án đăng ký quan tâm.
7. **Data sync:** Khi NĐT đăng ký/hủy quan tâm ở màn Chi tiết (§2.4) rồi quay lại Danh sách (§2.3), trạng thái nút trên Card tương ứng được cập nhật ngay (local state sync, không cần pull-to-refresh).
8. Thất bại → Hiển thị lỗi theo CMR-07.

#### 3.4 Xử lý lỗi (→ CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng / Mất kết nối | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + nút **"Thử lại"** | Giữ nguyên màn hình, hiển thị nút Thử lại. |
| Lỗi 401 (Session hết hạn) | *"Phiên đăng nhập hết hạn."* (Toast) | Auto refresh token. Nếu hết hạn >15 ngày → redirect Đăng nhập (CMR-07). |
| Lỗi 404 (Dữ liệu không tồn tại) | *"Nội dung không tồn tại hoặc đã bị xóa."* | Hiển thị thông báo tại vùng nội dung chính. Người dùng nhấn Quay lại để về Danh sách (CMR-07). |
| Lỗi API (HTTP 500) | *"Hệ thống đang bận. Vui lòng thử lại sau."* | Giữ nguyên màn hình. |
| Timeout (>10 giây) | *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + nút **"Thử lại"** | CMR-16. |
| Lỗi đăng ký/hủy quan tâm | *"Đăng ký quan tâm thất bại. Vui lòng thử lại."* / *"Hủy quan tâm thất bại. Vui lòng thử lại."* (Toast) | Nút giữ nguyên trạng thái trước khi nhấn. |
| Lỗi lưu thông tin NĐT (Form §2.2) | *"Lưu thông tin thất bại. Vui lòng thử lại."* (Toast) | Giữ nguyên form, không xoá dữ liệu đã nhập. |

#### 3.5 Đa ngôn ngữ (→ CMR-17)

Toàn bộ text cứng (header, label, placeholder, thông báo lỗi, empty state) dịch 5 ngôn ngữ: VI, EN, ZH, JA, KO. Nội dung dữ liệu từ API hiển thị nguyên bản.

---


### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Hub hiển thị 2 khối chức năng chính (Bổ sung thông tin + Danh sách đề xuất), điều hướng đúng.
- **AC2:** Form bổ sung thông tin: pre-fill dữ liệu cũ khi quay lại, validate trường bắt buộc, trường bắt buộc có dấu (*) đỏ bên cạnh label (CMR-09), matching realtime trả về kết quả.
- **AC3:** Matching Hybrid: kết quả phải khớp ít nhất 1 tiêu chí bắt buộc (Lĩnh vực HOẶC Địa bàn). Sắp xếp theo mức độ phù hợp giảm dần.
- **AC4:** Khi matching lại (sửa thông tin), danh sách cũ bị thay thế hoàn toàn.
- **AC5:** NĐT chưa bổ sung thông tin → vào Danh sách đề xuất → hiển thị empty state "Chưa có gợi ý dự án" + nút "Bổ sung ngay +" → tap điều hướng đến Màn hình Bổ sung thông tin NĐT (§2.2).
- **AC6:** Đăng ký quan tâm: không giới hạn số lượng, nút đổi trạng thái đúng. Hủy đăng ký hoạt động chính xác.
- **AC7:** Chi tiết dự án hiển thị đầy đủ 7 section thông tin theo wireframe, tất cả trường read-only, null → `-`.
- **AC8:** Phân biệt empty state: *"Không có dữ liệu."* (no data) vs *"Không tìm thấy kết quả."* (search/lọc rỗng) theo CMR-14.
- **AC9:** Tài liệu đính kèm tải/xem đúng (CMR-08).
- **AC10:** ~~NĐT nhận push notification khi có dự án mới được gán/matching.~~ → Chuyển sang UC Thông báo (UC riêng). UC87 không bao gồm luồng push notification.
- **AC11:** State Persistence: Khi quay lại từ chi tiết, danh sách giữ nguyên trạng thái tìm kiếm/lọc trước đó (CMR-01).

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-11 | v1 → v1.2 | Tạo SRS ban đầu | (Không có) | SRS đơn giản: danh sách + tìm kiếm + lọc | File UC87_TraCuuDuAnKeuGoiDauTu.md |
| 2026-05-15 | v1.2 → v1.3 | Viết lại toàn bộ theo input chi tiết | Chỉ có màn hình danh sách đơn giản | Bổ sung: Hub 3 chức năng, Form matching NĐT, Danh sách đề xuất + Đăng ký quan tâm, Chi tiết dự án đầy đủ (7 section), NĐT tự đề xuất | Rewrite theo requirement mới |
| 2026-05-15 | v1.3 → v1.4 | §2.1, §2.2, §2.3, §2.4 — Tham chiếu wireframe | (Không có) | Bổ sung tham chiếu wireframe: UC87 - Onboard.png, UC87 - Bổ sung thông tin.png, UC87 - Dự án đề xuất.png, UC87 - Chưa có gợi ý.png, UC87 - Filter dự án.png, UC87 - Chi tiết dự án.png | Wireframe mới nhất |
| 2026-05-15 | v1.3 → v1.4 | §2.2 Tiêu đề Header | "Bổ sung thông tin NĐT" | "Bổ sung thông tin" | Khớp wireframe |
| 2026-05-15 | v1.4 → v1.5 | §1 Phân quyền | Chỉ ghi "Cá nhân / Tổ chức (Logged-in)" | Bổ sung: "Cá nhân và Tổ chức có cùng giao diện và chức năng, không phân biệt." | Audit Q1 |
| 2026-05-15 | v1.4 → v1.5 | §4 AC10 | "NĐT nhận push notification khi có dự án mới" | Chuyển sang UC Thông báo (UC riêng). UC87 không bao gồm push notification. | Audit Q2 |
| 2026-05-15 | v1.4 → v1.5 | §2.2 Multi-select | Không mô tả giới hạn và hiển thị | Không giới hạn số lượng, hiển thị dạng chip/tag, wrap xuống dòng | Audit Q4 |
| 2026-05-15 | v1.4 → v1.5 | §2.2 #7 Quy mô vốn | "Đơn vị: VNĐ hoặc USD (chọn bên cạnh)" | "Đơn vị: VNĐ (cố định)" — wireframe không có dropdown đơn vị | Audit Q5 |
| 2026-05-15 | v1.4 → v1.5 | §3.3 Data sync | (Không có) | Bổ sung: quay lại Danh sách từ Chi tiết → trạng thái nút cập nhật ngay (local state sync) | Audit Q6 |
| 2026-05-15 | v1.4 → v1.5 | §2.4 #13 Link null | "Null → Ẩn field" (không giải thích) | Bổ sung: "Exception CMR-14: field Link/Tappable → ẩn khi null" | Audit Q8 |
| 2026-05-15 | v1.4 → v1.5 | §3.1 step 5 Matching | "Bắt buộc: dự án phải khớp ít nhất 1 tiêu chí bắt buộc (Lĩnh vực HOẶC Địa bàn)" | Viết lại rõ: "Form bắt buộc điền cả 2. Matching chỉ cần khớp ít nhất 1 trong 2 để đưa vào kết quả." | Audit Q9 |
| 2026-05-15 | v1.4 → v1.5 | §2.2 Back dirty form | (Không có) | ~~CMR-10 đã bị xóa~~ | Audit Q10 |
| 2026-05-15 | v1.4 → v1.5 | §2.1 #3 Icon Chuông | "Badge đỏ khi có thông báo mới" | "Badge dạng dot đỏ (không hiển thị số)" + ref UC Thông báo riêng | Audit Q13 |
| 2026-05-18 | v1.5 → v1.6 | §2.3 #3 Ô tìm kiếm Placeholder | "Tìm kiếm dự án..." | "Tìm kiếm nhanh theo tên dự án, mã dự án" | CMR-01 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 #9 Textarea Placeholder | "Mô tả chi tiết nhu cầu đầu tư của bạn..." | "Nhập mô tả nhu cầu đầu tư" | CMR-09 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 #7 Textbox Placeholder | (Không có) | "Nhập quy mô vốn dự kiến" | CMR-09 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 #7, #9 Message lỗi Max length | (Không có) | Bổ sung: "[Tên trường] nhập quá ký tự cho phép" | CMR-09 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 Dropdown Placeholder | "Chọn lĩnh vực quan tâm...", "Chọn ngành kinh tế..." (có dấu ...) | Bỏ dấu "..." theo chuẩn: "Chọn [tên trường]" | CMR-03 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.3, §2.4 CMR-11 | Chỉ ghi ref "(CMR-11)" | Mô tả rõ: "Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm" | CMR-11 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.3 Filter Dropdown Placeholder | (Không có) | Bổ sung Placeholder: "Chọn [tên trường]" cho tất cả dropdown trong bộ lọc | CMR-03 chuẩn MBFS |
| 2026-05-19 | v1.6 → v1.7 | §2.3 #13, §2.4 #50 — Button loading state | (Không có) | Bổ sung: Khi đang chờ API → button disabled + spinner cục bộ thay text (CMR-07) | QC feedback Q1 |
| 2026-05-20 | v1.7 → v1.8 | §2.3 Tham chiếu wireframe Empty state | (Không có) | Bổ sung tham chiếu `UC87 - Dự án đề xuất - Empty state.png` vào header §2.3 | QC feedback |
| 2026-05-20 | v1.7 → v1.8 | §2.3 Trạng thái đặc biệt — Danh sách rỗng | (Không có) | Bổ sung: "Nếu matching không trả về kết quả hoặc tìm kiếm/lọc rỗng → hiển thị hình ảnh trống + 'Không có dữ liệu.' (CMR-14)" | QC feedback Q2 |
| 2026-05-20 | v1.7 → v1.8 | §2.4 Quy tắc chung hiển thị Section | (Không có) | Bổ sung: "Section 1-6 luôn hiển thị, field null → '-'. Section 7 ẩn toàn bộ khi không có file." | QC feedback Q2 |
| 2026-05-20 | v1.7 → v1.8 | §2.2 #7 Quy mô vốn — Validation > 0 | "Chỉ nhập số" | "Chỉ nhập số nguyên dương > 0 (không chấp nhận số âm, số 0 hay ký tự đặc biệt)" + message lỗi: "Quy mô vốn dự kiến phải lớn hơn 0" | QC feedback Q3 |
| 2026-05-20 | v1.7 → v1.8 | §1 Phân quyền — Role không hợp lệ | (Không có) | Bổ sung: "Token chứa role không hợp lệ → xử lý như lỗi 401 theo CMR-07" | QC feedback Q4 |
| 2026-05-20 | v1.7 → v1.8 | §1 Postconditions | "Hệ thống hiển thị danh sách dự án phù hợp hoặc cho phép NĐT đăng ký quan tâm dự án." | Tách rõ 3 postconditions: (a) sau bổ sung thông tin, (b) sau đăng ký quan tâm, (c) sau hủy quan tâm | QC feedback Q5 |
| 2026-05-20 | v1.7 → v1.8 | §3.3 step 3 — Loading + Debounce | "Hệ thống gọi API đăng ký quan tâm." (chỉ 1 dòng) | Bổ sung mô tả: loading trên button (disabled + spinner) + Debounce (CMR-18) chỉ nhận action đầu tiên | QC feedback Q1 (tích hợp vào luồng) |
| 2026-05-20 | v1.8 → v1.9 | §2.1 #3 — Badge thông báo | Badge dạng dot đỏ | Badge dạng dot vàng | QC feedback Q1 |
| 2026-05-20 | v1.8 → v1.9 | §2.1 #4, #5 — Nút action trên Card | Chỉ mô tả "Tap card → Điều hướng" | Bổ sung nút "Cập nhật" (Card 1) và "Xem danh sách" (Card 2) | QC feedback Q2 |
| 2026-05-20 | v1.8 → v1.9 | §2.2 #3 — Lĩnh vực quan tâm Searchable | Không có Searchable | Bổ sung Searchable (CMR-03) | QC feedback Q3/Q8 |
| 2026-05-20 | v1.8 → v1.9 | §2.2 Dropdown — Giá trị mặc định | Placeholder: "Chọn [tên trường]" | Giá trị mặc định: "Tất cả" cho tất cả dropdown (form + filter) | QC feedback Q4/Q6 |
| 2026-05-20 | v1.8 → v1.9 | §2.2 Multi-select — Chip/tag đồng nhất | Row 4, 8 chưa mô tả đầy đủ chip/tag | Bổ sung: "wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa." cho tất cả multi-select | QC feedback Q8 |
| 2026-05-20 | v1.8 → v1.9 | §2.3 Filter — Xóa Placeholder | Có Placeholder: "Chọn [tên trường]" | Xóa Placeholder, chỉ giữ giá trị mặc định "Tất cả" | QC feedback Q6 |
| 2026-05-20 | v1.9 → v2.0 | §2.3 — Tham chiếu wireframe Huỷ quan tâm | (Không có) | Bổ sung tham chiếu `UC87 - Dự án đề xuất - Huỷ quan tâm.png` vào header §2.3 và mô tả nút "Hủy quan tâm" | Wireframe mới |
| 2026-05-20 | v1.9 → v2.0 | §2.4 — Đồng bộ Chi tiết với wireframe | 7 section, 50 trường, gồm Bảng hạng mục chi phí và Bảng mốc kế hoạch | 7 section, 30 trường — cắt giảm hoàn toàn theo wireframe `UC87 - Chi tiết dự án.png`. Xoá: Loại dự án, Ngành kinh tế, Quốc gia triển khai, Địa bàn ưu đãi, Chính sách ưu đãi/hỗ trợ, Link quảng bá, Bảng chi phí, Bảng mốc kế hoạch, v.v. Thêm: Cơ quan chủ quản, Đơn vị triển khai, Công suất, Vốn tư nhân/FDI, Tình trạng hiện tại | Đồng bộ WF |
| 2026-05-20 | v1.9 → v2.0 | §2.4 — Quy tắc read-only + text dài | (Không có) | Bổ sung: tất cả trường read-only, text dài hiển thị đầy đủ (text wrap, không truncate). Email/SĐT hiển thị dạng text thuần (không phải link tappable) | Q1 |
| 2026-05-20 | v1.9 → v2.0 | §2.3 — Button "Bổ sung ngay" | Chỉ ghi "nút Bổ sung ngay (tap → điều hướng đến Màn hình 2.2)" | Mô tả chi tiết: tiêu đề "Chưa có gợi ý dự án", mô tả, nút "Bổ sung ngay +" (nền đỏ đậm, icon "+", Debounce CMR-18) | Q2 |
| 2026-05-20 | v1.9 → v2.0 | §3.4 — Bổ sung case xử lý lỗi | 4 case (mạng, 401, 500, timeout) | 7 case — bổ sung: Lỗi 404, Lỗi đăng ký/hủy quan tâm, Lỗi lưu thông tin NĐT | Q3, CMR-07 |
| 2026-05-20 | v1.9 → v2.0 | §2.3, §3.2 — Phân biệt empty state | Gộp chung "Không có dữ liệu." cho cả no data và search/lọc rỗng | Tách: "Không có dữ liệu." (no data) vs "Không tìm thấy kết quả." (search/lọc rỗng) theo CMR-14 | Q4 |
| 2026-05-20 | v1.9 → v2.0 | §2.3 — State Persistence | (Không có) | Bổ sung: quay lại từ chi tiết → giữ nguyên trạng thái tìm kiếm, bộ lọc, vị trí scroll (CMR-01) | Q5 |
| 2026-05-20 | v1.9 → v2.0 | §2.2 — Dấu (*) trường bắt buộc | (Không có) | Bổ sung: tất cả trường bắt buộc hiển thị dấu (*) màu đỏ bên cạnh label (CMR-09) | Q6 |
| 2026-05-21 | v2.0 → v2.1 | §2.3 — Placeholder tìm kiếm | "Tìm kiếm nhanh theo tên dự án, mã dự án" | "Tìm kiếm nhanh theo tên dự án" — Bỏ "mã dự án" vì Card dự án không hiển thị mã | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.3 — Trường Tổng vốn đầu tư dự kiến trên Card | Icon $ + Số tiền (màu đỏ) | Icon tiền (₫) + "Vốn: " + Số tiền (màu đỏ) + "tỷ VNĐ" — theo wireframe | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.3 — Trường Ngày đăng ký trên Card | Label, Format: dd/MM/yyyy | Icon + Label: Icon lịch + "Đăng ký: " + dd/MM/yyyy — theo wireframe | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.4 Section 1 — Tiêu đề section | (Không có) | Bổ sung dòng "Tiêu đề section" (#3) với giá trị "1. Thông tin chung", font đậm, màu đỏ đậm — đồng bộ với Section 2-7 | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.4 Section 1 — Mô tả chi tiết | Lĩnh vực, Địa bàn, Hình thức đầu tư chỉ ghi "Null → - (CMR-14)" | Bổ sung Quy tắc hiển thị đầy đủ: font, text wrap, mô tả rõ ràng | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.4 Section 2-7 — Đồng bộ Tiêu đề section | Tiêu đề section không có số thứ tự, format cũ | Cập nhật giá trị mặc định thêm số thứ tự ("2. Cơ quan quản lý", "3. Thông tin liên hệ"...), bổ sung quy tắc hiển thị: font đậm, màu đỏ đậm — khớp wireframe | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.4 — Đánh số lại | #3-30 (30 trường) | #3-31 (31 trường) — do thêm dòng Tiêu đề Section 1 | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.3, §3.1 — CMR-14 empty state | §2.3: "hệ thống không có dự án phù hợp hoặc chưa có dự án nào được gán"; §3.1 bước 7: "Không có dữ liệu." | §2.3: "hệ thống chưa có dự án kêu gọi đầu tư nào"; §3.1 bước 7: "Không tìm thấy kết quả." (matching = filter behavior) | QC feedback |
| 2026-05-21 | v2.0 → v2.1 | §2.2 — Trạng thái mặc định form | (Không có) | Bổ sung mô tả trạng thái mặc định khi NĐT mở form lần đầu: Lĩnh vực "Tất cả", các dropdown khác "Tất cả", textbox/textarea trống — theo wireframe | QC feedback |
| 2026-05-21 | v2.1 → v2.2 | §2.3 #7, #8 — Màu text trên Card | Không mô tả màu | Bổ sung: "Font nhỏ, màu xám." cho Lĩnh vực và Địa bàn | QC feedback |
| 2026-05-21 | v2.1 → v2.2 | §2.3 #9 — Màu chi tiết Tổng vốn | "tiền tố 'Vốn: ' + Số tiền (màu đỏ) + đơn vị 'tỷ VNĐ'" | Bổ sung: tiền tố "Vốn: " (màu xám) + Số tiền (màu đỏ) + đơn vị "tỷ VNĐ" (màu xám). Font nhỏ. | QC feedback — theo wireframe |
| 2026-05-21 | v2.1 → v2.2 | §2.3 — No data empty state | "API trả về danh sách rỗng ngay từ đầu, không qua filter/search" | "API trả về danh sách rỗng ngay từ đầu dù user đã sử dụng filter/search" | QC feedback |
| 2026-05-21 | v2.2 → v2.3 | Align CMR Mobile v6.0 | 1. Search box max 500→255. 2. Quy mô vốn dự kiến max 500→255. 3. Nút "Xem dự án phù hợp" Disabled→Luôn Enabled. 4. Bỏ dấu "." cuối inline validation errors. 5. Bổ sung CMR-03 cho Searchable Dropdown. |
| 2026-05-21 | v2.2 → v2.3 | Dropdown filter | Giá trị mặc định "Tất cả [tên trường]"→"Tất cả". |
| 2026-05-21 | v2.2 → v2.3 | Align CMR Mobile v6.0 | 1. Search box max length 500→255 |
| 2026-05-21 | v2.2 → v2.3 | Clean up incorrect CMR references | Xoá các mã tracking (D07, D08, I01), thay thế bằng mã chuẩn CMR |
| 2026-05-21 | v2.2 → v2.3 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v2.2 → v2.3 | Align CMR Mobile v1.9 — Fix body inconsistencies | 1. §2.2 Trạng thái mặc định: Nút "Xem dự án phù hợp" Disabled→Luôn Enabled (CMR-09 I01) — đồng bộ với §2.2 #10. 2. §2.2 #7 Quy mô vốn: error format `"nhập quá ký tự cho phép"` → `"không được vượt quá 255 ký tự!"` (CMR-09). 3. §2.2 #9 Mô tả nhu cầu: error format → `"không được vượt quá 2000 ký tự!"` (CMR-09). |
| 2026-05-22 | v2.2 → v2.3 | §2.2 Multi-select — Hành vi option đã chọn | Không mô tả hành vi option sau khi chọn | Bổ sung: "Option đã chọn sẽ bị ẩn (remove) khỏi danh sách dropdown. Khi user xóa chip (tap X) → option tương ứng quay lại danh sách dropdown." cho tất cả Dropdown (Multi-select): #3, #4, #5, #8 | QC feedback — clarify multi-select UX |
| 2026-05-22 | v2.2 → v2.3 | §2.2 #6, §2.3 #13-#17 — Single-select highlight | Không mô tả hành vi highlight option đã chọn | Bổ sung: "Single-select: Tap 1 option → thay thế giá trị hiện tại → đóng dropdown. Option đã chọn được highlight/bold khi mở lại dropdown list (CMR-03)." cho tất cả Dropdown single-select | QC feedback — clarify single-select UX |
| 2026-05-22 | v2.2 → v2.3 | §2.4 #30 — Bỏ nút "Tải xuống" tài liệu đính kèm | Mỗi item: Icon loại file + Tên tài liệu + Nút "Tải xuống" (icon download). Tap nút "Tải xuống" → Xem/Tải | Mỗi item: Icon loại file (📄) + Tên tài liệu. Không có nút "Tải xuống" riêng. Tap vào item tài liệu → Xem/Tải theo CMR-08. | Đồng bộ wireframe — màn Chi tiết dự án đã bỏ nút Download |
| 2026-05-22 | v2.2 → v2.3 | §2.1 #3 — Bỏ Icon Thông báo (Chuông) | Dòng #3: Icon Thông báo (Chuông) với Badge dot vàng, tap → Trung tâm thông báo | Xóa hoàn toàn dòng #3. Đánh lại STT: Card "Bổ sung thông tin NĐT" → #3, Card "Danh sách dự án đề xuất" → #4 | Đồng bộ wireframe — màn Onboard đã bỏ icon Noti |
| 2026-05-24 | v2.2 → v2.3 | §2.2 #3, #5 — Bỏ inline error unreachable | #3: "Inline error nếu bỏ trống: Vui lòng chọn lĩnh vực quan tâm"; #5: "Inline error nếu bỏ trống: Vui lòng chọn địa bàn mong muốn" | Bỏ inline error. Bổ sung lưu ý: trường luôn có giá trị (fallback "Tất cả" khi rỗng) → trạng thái bỏ trống không xảy ra → inline error unreachable | QC feedback — logic contradiction: CMR-03 "Tap ra ngoài khi rỗng → chọn lại Tất cả" khiến field không bao giờ empty |
| 2026-05-24 | v2.2 → v2.3 | §2.2 #7, §3.1 — Đơn vị vốn và logic matching | §2.2 Đơn vị: VNĐ. §3.1 Chưa định nghĩa rõ logic matching vốn. | §2.2 Đổi đơn vị thành 'tỷ VNĐ'. §3.1 Bổ sung logic matching Quy mô vốn: dự án được ưu tiên nếu vốn nằm trong dung sai +/- 20% so với NĐT nhập | QC feedback + update UI wireframe |
| 2026-05-24 | v2.2 → v2.3 | §2.4 — Bổ sung trường thiếu theo wireframe | Màn hình chi tiết không có Loại dự án, Ngành kinh tế | Bổ sung Loại dự án và Ngành kinh tế vào Section 1 (Thông tin chung) để đồng bộ tiêu chí filter. Đánh số lại từ #9 đến #32 | QC feedback + update UI wireframe |
