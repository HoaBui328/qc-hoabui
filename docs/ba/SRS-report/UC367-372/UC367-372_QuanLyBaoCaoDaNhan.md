# UC367-372: Quản lý báo cáo đã nhận

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | (Chưa xác định) |
| **Phân hệ** | Tất cả (Cross-phân hệ) |
| **Mẫu biểu** | N/A — Màn hình tổng hợp quản lý báo cáo đã nhận (Admin side) |
| **Loại báo cáo** | N/A (Áp dụng cho tất cả loại báo cáo đã nhận) |
| **Hình thức nộp** | N/A |
| **Phạm vi dữ liệu đầu vào** | Không |
| **Cơ quan nhận** | N/A |
| **Đối tượng lập** | N/A (Đây là màn hình quản lý phía Admin) |
| **Giao diện** | Admin site (Phía quản trị — Đơn vị tiếp nhận báo cáo) |
| **Ngày tạo** | 2026-05-15 |
| **Phiên bản** | 1.4 |

---

## Phạm vi (Scope)

### In Scope
- UC367: Xem danh sách báo cáo đã nhận + Lọc (Search, Filter Phân hệ, Filter Đơn vị nộp, Filter Ngày nộp date-range, Filter Trạng thái, Xuất Excel)
- UC368: Xem chi tiết báo cáo (Full-page read-only, CF_07)
- UC369: Phản hồi báo cáo (YCCS / Phê duyệt / Chỉnh sửa) + Xem trước (CF_01) + Xuất báo cáo (CF_04) + Xem vòng đời (CF_06)
- UC370: Xem danh sách báo cáo Địa phương đã nộp (gộp chung danh sách với NĐT)
- UC371: Xem chi tiết báo cáo Địa phương (tương tự UC368)
- UC372: Phản hồi báo cáo Địa phương (tương tự UC369)
- 4 Summary Cards thống kê theo trạng thái
- Pagination 10/20/50/100

### Out of Scope
- Tạo mới báo cáo (thuộc luồng NĐT — UC364-366)
- Xử lý xung đột đồng thời phức tạp (giả định 1 Admin/cơ quan)
- Thiết kế template Email thông báo (Pending — ghi nhận tại NFR)
- Quản lý quyền Admin (thuộc module phân quyền riêng)

---

## Điều kiện tiên quyết & Hậu điều kiện

### Preconditions
1. User đã đăng nhập thành công vào hệ thống.
2. User có quyền truy cập module "Báo cáo đã nhận" (menu sidebar).
3. User thuộc một trong hai loại đơn vị:
   - **Đơn vị trung gian phê duyệt**: Có quyền Phê duyệt / Yêu cầu chỉnh sửa.
   - **Đơn vị đích nhận**: Có quyền Chỉnh sửa (tự chỉnh sửa) / Yêu cầu chỉnh sửa.

### Postconditions

| Sau khi hoàn thành... | Trạng thái hệ thống |
|----------------------|---------------------|
| Phê duyệt (Đơn vị trung gian) | TT = "Đã tiếp nhận" (final). NĐT/Địa phương nhận thông báo. Card "Đã tiếp nhận" +1, card "Chờ duyệt" -1. |
| Yêu cầu chỉnh sửa | TT = "Yêu cầu chỉnh sửa". NĐT/Địa phương nhận thông báo. Form NĐT/Địa phương enable cho phép nộp lại. |
| NĐT/Địa phương Nộp lại | TT = "Chờ duyệt". Admin nhận thông báo. Card "Chờ duyệt" +1, card "YCCS" -1. |

---

## UC367-372.1: Xem Danh Sách Báo Cáo Đã Nhận + Lọc

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo đã nhận
- Chức năng cho phép User (thuộc đơn vị trung gian phê duyệt hoặc đơn vị đích nhận) quản lý các báo cáo mà đơn vị của user login là đơn vị trung gian hoặc đơn vị đích trong luồng phê duyệt. Báo cáo có thể được nộp bởi Nhà đầu tư, Tổ chức kinh tế, hoặc các cấp địa phương, theo luồng phê duyệt. User có thể theo dõi trạng thái xử lý (Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa), và thực hiện lọc/tìm kiếm.

Phân quyền: User thuộc đơn vị trung gian phê duyệt hoặc đơn vị đích nhận.

Truy cập chức năng: Menu sidebar → Báo cáo đã nhận

Chức năng đáp ứng usecase số: 367, 368, 369, 370, 371, 372

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **SUMMARY CARDS (Thống kê)** | | | | | | |
| 1 | Tổng đã nhận | Card (Integer) | Giá trị thực tế | | | Tổng hợp tất cả báo cáo đã nhận (Chờ duyệt + Đã tiếp nhận + YCCS). Số liệu tính lại khi load trang, **không thay đổi** khi user thao tác filter. Click → reset filter trạng thái, grid hiển thị tất cả. Active state: border-left đậm + font-weight bold. |
| 2 | Chờ duyệt | Card (Integer) | Giá trị thực tế | | | Số báo cáo đang chờ xử lý. Số cố định (không đổi khi filter). Click → grid lọc chỉ hiển thị Chờ duyệt. Active state: border-left đậm + font-weight bold. **Mặc định active khi load trang.** |
| 3 | Yêu cầu chỉnh sửa | Card (Integer) | Giá trị thực tế | | | Số báo cáo đang yêu cầu NĐT/Địa phương bổ sung/chỉnh sửa. Số cố định. Click → grid lọc chỉ hiển thị YCCS. Active state: border-left đậm + font-weight bold. |
| 4 | Đã tiếp nhận | Card (Integer) | Giá trị thực tế | | | Số báo cáo đã được phê duyệt (final state). Số cố định. Click → grid lọc chỉ hiển thị Đã tiếp nhận. Active state: border-left đậm + font-weight bold. |
| **BỘ LỌC & TÌM KIẾM** | | | | | | |
| 5 | Tìm kiếm | Search bar | Null | x | | Placeholder: "Tìm kiếm nhanh theo mã báo cáo, tên báo cáo". Max 255 ký tự. Phạm vi tìm: Mã báo cáo + Tên báo cáo. Partial match, case-insensitive, live search (debounce 300-500ms). Không tìm thấy → hiển thị Empty State. Tham chiếu: CMR_06, CMR_18. |
| 6 | Phân hệ | Dropdown | Tất cả | x | | Giá trị: Tất cả / ĐT nước ngoài vào VN / ĐT VN ra nước ngoài / Xúc tiến ĐT / KCN/Khu KT. Chọn → grid lọc ngay (real-time). Tham chiếu: CMR_07, CMR_16. |
| 7 | Trạng thái | Dropdown | Chờ duyệt | x | | Giá trị: Tất cả / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. **Mặc định: Chờ duyệt.** Đồng bộ 2 chiều với Summary Cards. Tham chiếu: CMR_07, CMR_16. |
| 8 | Đơn vị nộp | Dropdown | Tất cả | x | | Giá trị: Tất cả / Danh sách đơn vị nộp (lấy từ dữ liệu thực tế). Chọn → grid lọc ngay (real-time). Tham chiếu: CMR_07, CMR_16. |
| 9 | Ngày nộp | Date range picker | Null | x | | Gồm 2 ô: "Từ ngày" và "Đến ngày". Định dạng: dd/MM/yyyy. Chọn → grid lọc ngay (real-time). Tham chiếu: CMR_07. |
| 10 | Xuất Excel | Button (đỏ) | | | | Xuất toàn bộ danh sách báo cáo (theo filter hiện tại) ra file .xlsx. |
| **BẢNG DỮ LIỆU (GRID)** | | | | | | |
| 11 | STT | Integer (auto) | Null | | | Đánh số tự động theo trang hiện tại. Trang 1: 1-10, Trang 2: 11-20... |
| 12 | Mã báo cáo | Label (link) | Null | | | Clickable — nhấn vào điều hướng đến màn hình Xem chi tiết (UC367-372.2). Tham chiếu: CMR_09. |
| 13 | Tên báo cáo | Label | Null | | | Hiển thị tên đầy đủ của báo cáo. Max-width 250px. Text vượt quá → cắt ngắn + ellipsis (...). Hover → tooltip hiển thị full text. |
| 14 | Phân hệ | Badge màu | Null | | | Hiển thị tên phân hệ dưới dạng badge. Mỗi phân hệ có màu riêng: ĐT nước ngoài vào VN = xanh dương, ĐT VN ra nước ngoài = xanh lá, Xúc tiến ĐT = vàng, KCN/Khu KT = tím. |
| 15 | Kỳ báo cáo | Label | Null | | | Hiển thị kỳ báo cáo. VD: "Quý 1/2026", "Năm 2025", "6T đầu/2026". |
| 16 | Đơn vị nộp | Label | Null | | | Hiển thị tên đơn vị cụ thể của người nộp. VD đơn vị địa phương: "UBND tỉnh Bình Dương", "Cục Thuế tỉnh Bắc Ninh", "Sở KH&ĐT tỉnh Đồng Nai". VD tổ chức kinh tế: "Công ty TNHH ABC", "Công ty CP XYZ". Nếu người nộp là cá nhân nhà đầu tư (không phải tổ chức) → hiển thị full name cá nhân (VD: "Nguyễn Văn Minh", "Trần Thị Hương Lan"). |
| 17 | Ngày nộp | Label | Null | | | Định dạng: dd/MM/yyyy. Hiển thị ngày nộp gần nhất. Hỗ trợ sort: icon sort (↓/↑) trên header. Mặc định: Descending (mới nhất lên đầu). |
| 18 | Trạng thái | Badge màu | Null | | | Chờ duyệt = badge vàng. Đã tiếp nhận = badge xanh lá. YCCS = badge cam. |
| 19 | Thao tác | Button group | Null | | | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết: xem bảng Action Mapping bên dưới. |
| **PHÂN TRANG** | | | | | | |
| 20 | Phân trang | Pagination | 10 báo cáo/trang | | | Dropdown chọn: 10 / 20 / 50 / 100 bản ghi/trang. Hiển thị text: "Hiển thị [start]-[end] / [total] báo cáo". Button [Trang trước]: Disabled khi ở trang 1. Button [Trang sau]: Disabled khi ở trang cuối. Tham chiếu: CMR_10. |

**Action Mapping — Cột Thao tác (tại Danh sách):**

| # | Tên | Kiểu | Điều kiện hiển thị | Mô tả |
| --- | --- | --- | --- | --- |
| 1 | Xem chi tiết | Text link | Tất cả trạng thái | Điều hướng đến màn hình Xem chi tiết (UC367-372.2). |
| 2 | Xem vòng đời | Icon button | Tất cả trạng thái | Mở popup timeline. Tham chiếu: CF_06. |
| 3 | Chỉnh sửa | Text link | TT = "Đã tiếp nhận" | Điều hướng đến màn hình chỉnh sửa báo cáo. Chỉ hiển thị khi báo cáo đã được tiếp nhận. |
| 4 | In | Icon button | Tất cả trạng thái | Mở print preview (browser print dialog). |
| 5 | Export | Icon button | Tất cả trạng thái | Kết xuất báo cáo ra file. Tham chiếu: CF_04. |

---

### 3. Mô tả các xử lý của chức năng

- Phạm vi hiển thị dữ liệu:
  - Danh sách hiển thị tất cả báo cáo đã được NĐT/Địa phương nộp thành công vào hệ thống mà User có quyền quản lý.
  - Dữ liệu cross-phân hệ: hiển thị báo cáo từ tất cả phân hệ.
  - Không phân biệt NĐT/Địa phương — hiển thị gộp chung trong 1 danh sách.

- **Mặc định khi load trang:**
  - Danh sách mặc định hiển thị báo cáo ở trạng thái **"Chờ duyệt"**.
  - Card "Chờ duyệt" mặc định ở trạng thái active.
  - Dropdown Trạng thái mặc định = "Chờ duyệt".

- Logic Summary Cards:
  - Số liệu trên 4 cards được tính lại từ API mỗi khi load/reload trang.
  - Số liệu **không thay đổi** khi user thao tác filter (Search / Ngày nộp / Phân hệ / Đơn vị nộp) trong session hiện tại.
  - Đồng bộ 2 chiều với dropdown Trạng thái: user thay đổi dropdown → card active cập nhật tương ứng. User chọn "Tất cả" → card "Tổng đã nhận" active.
  - Click vào card → grid lọc theo trạng thái tương ứng, dropdown Trạng thái tự động cập nhật.

- Logic bộ lọc:
  - Tất cả bộ lọc hoạt động đồng thời (AND logic). Grid chỉ hiển thị bản ghi thỏa mãn TẤT CẢ điều kiện filter đang active.
  - Search bar áp dụng Debounce 300-500ms sau khi người dùng ngừng gõ. Tham chiếu: CMR_06, CMR_18.
  - Dropdown Phân hệ, Trạng thái, Đơn vị nộp và Date range Ngày nộp lọc ngay khi chọn (real-time). Tham chiếu: CMR_07.

- Xuất Excel:
  - Nhấn nút [Xuất Excel] → Hệ thống xuất danh sách báo cáo (theo filter hiện tại) ra file .xlsx.
  - Thành công: Toast — *"Đã xuất Excel thành công"*.
  - Thất bại: Toast lỗi — *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"*

- Empty State:
  - **Empty State A** (chưa có báo cáo nào được nộp): Icon document xám. Tiêu đề: "Chưa có báo cáo nào". Mô tả: "Các báo cáo sau khi được nộp bởi Nhà đầu tư hoặc Địa phương sẽ hiển thị tại đây." Summary Cards: Tất cả hiển thị "0", giữ nguyên color coding mặc định.
  - **Empty State B** (search/filter không có kết quả): Icon search xám. Tiêu đề: "Không tìm thấy dữ liệu". Mô tả: "Thử thay đổi từ khóa hoặc bộ lọc để tìm báo cáo phù hợp"

- Sắp xếp mặc định: Theo Ngày nộp giảm dần (mới nhất lên đầu). Sort áp dụng trên toàn bộ dataset (không chỉ trang hiện tại).

---


## UC367-372.2: Xem Chi Tiết Báo Cáo Đã Nhận

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem chi tiết báo cáo đã nhận
- Chức năng cho phép User xem toàn bộ nội dung báo cáo đã nộp ở chế độ read-only (full-page). Hiển thị đầy đủ dữ liệu đã nộp theo đúng biểu mẫu tương ứng. Tại đây User có thể thực hiện các hành động phản hồi tùy theo loại đơn vị.

Phân quyền: User thuộc đơn vị trung gian phê duyệt hoặc đơn vị đích nhận.

Truy cập chức năng: Màn danh sách (UC367-372.1) → Click Mã báo cáo hoặc nút [Xem chi tiết]

Chức năng đáp ứng usecase số: 368, 371

---

### 2. Mô tả giao diện

**Màn hình xem chi tiết (Full-page, Read-only)**

Tham chiếu: CF_07 (mở rộng — full-page mode).

Giao diện hiển thị toàn bộ dữ liệu báo cáo theo đúng biểu mẫu tương ứng. Tất cả trường ở trạng thái Disabled (không cho phép chỉnh sửa). Không áp dụng validation rule — đây là màn hình read-only thuần túy. Chi tiết các fields hiển thị tùy thuộc vào loại biểu mẫu được nộp (tham chiếu UC tương ứng của từng biểu mẫu).

**Bottom Action Bar — Đơn vị trung gian phê duyệt:**

| # | Tên | Kiểu | Điều kiện hiển thị | Mô tả |
| --- | --- | --- | --- | --- |
| 1 | Hủy | Button Outline | Tất cả trạng thái | Điều hướng về màn hình Danh sách (UC367-372.1). Không cần popup xác nhận. |
| 2 | Yêu cầu chỉnh sửa | Button Warning | TT = Chờ duyệt hoặc YCCS | Mở Popup xác nhận YCCS. Chi tiết: UC367-372.3. |
| 3 | Phê duyệt | Button Success | TT = Chờ duyệt hoặc YCCS | Mở Popup xác nhận Phê duyệt. Chi tiết: UC367-372.3. |
| 4 | Xem trước | Button Outline | Tất cả trạng thái | Mở popup preview PDF read-only. Tham chiếu: CF_01. |
| 5 | Export | Button Outline | Tất cả trạng thái | Kết xuất file theo CF_04. |
| 6 | Xem vòng đời báo cáo | Button Outline | Tất cả trạng thái | Mở popup timeline. Tham chiếu: CF_06. |

**Bottom Action Bar — Đơn vị đích nhận:**

| # | Tên | Kiểu | Điều kiện hiển thị | Mô tả |
| --- | --- | --- | --- | --- |
| 1 | Hủy | Button Outline | Tất cả trạng thái | Điều hướng về màn hình Danh sách (UC367-372.1). Không cần popup xác nhận. |
| 2 | Yêu cầu chỉnh sửa | Button Warning | TT = Chờ duyệt hoặc YCCS | Mở Popup xác nhận YCCS. Chi tiết: UC367-372.3. |
| 3 | Chỉnh sửa | Button Primary | TT = Đã tiếp nhận | Chuyển sang chế độ chỉnh sửa báo cáo (đơn vị đích tự chỉnh sửa nội dung). |
| 4 | Xem trước | Button Outline | Tất cả trạng thái | Mở popup preview PDF read-only. Tham chiếu: CF_01. |
| 5 | Export | Button Outline | Tất cả trạng thái | Kết xuất file theo CF_04. |
| 6 | Xem vòng đời báo cáo | Button Outline | Tất cả trạng thái | Mở popup timeline. Tham chiếu: CF_06. |

---

### 3. Mô tả các xử lý của chức năng

- Nhấn Mã báo cáo (link) hoặc [Xem chi tiết] → Hệ thống điều hướng đến màn hình xem chi tiết full-page (read-only).
- Hiển thị toàn bộ dữ liệu báo cáo theo đúng biểu mẫu tương ứng. Tất cả trường ở trạng thái Disabled.
- Bottom Action Bar hiển thị các nút hành động **tùy theo loại đơn vị của user login**:
  - **Đơn vị trung gian phê duyệt:**
    - TT = Chờ duyệt hoặc YCCS: Hiển thị [Hủy], [YCCS], [Phê duyệt], [Xem trước], [Export], [Xem vòng đời].
    - TT = Đã tiếp nhận (final state): Ẩn [YCCS], [Phê duyệt]. Chỉ hiển thị [Hủy], [Xem trước], [Export], [Xem vòng đời].
  - **Đơn vị đích nhận:**
    - TT = Chờ duyệt hoặc YCCS: Hiển thị [Hủy], [YCCS], [Xem trước], [Export], [Xem vòng đời]. (Không có nút Chỉnh sửa vì chưa tiếp nhận.)
    - TT = Đã tiếp nhận: Hiển thị [Hủy], [Chỉnh sửa], [Xem trước], [Export], [Xem vòng đời]. Ẩn [YCCS].
- Xem trước: Tham chiếu CF_01. Mở popup preview PDF read-only.
- Export: Tham chiếu CF_04. Kết xuất file .docx hoặc .xlsx tùy biểu mẫu.
- Xem vòng đời: Tham chiếu CF_06.
- Hủy: Điều hướng về màn hình Danh sách. Không cần popup xác nhận (User chỉ xem, không có dữ liệu chưa lưu).

---

## UC367-372.3: Phản Hồi Báo Cáo + Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Phản hồi báo cáo đã nhận và các tác vụ bổ trợ
- Chức năng cho phép User thực hiện các hành động phản hồi đối với báo cáo đã nộp:
  - **Đơn vị trung gian phê duyệt**: Yêu cầu chỉnh sửa, Phê duyệt.
  - **Đơn vị đích nhận**: Yêu cầu chỉnh sửa, Chỉnh sửa (tự chỉnh sửa).
- Kèm theo các tác vụ bổ trợ: Xem trước (CF_01), Xuất báo cáo (CF_04), Xem vòng đời báo cáo (CF_06).

Phân quyền: User thuộc đơn vị trung gian phê duyệt hoặc đơn vị đích nhận.

Truy cập chức năng: Màn chi tiết (UC367-372.2) → Bottom Action Bar

Chức năng đáp ứng usecase số: 369, 372

---
### 2. Mô tả giao diện

**Popup Xác nhận Phê duyệt:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Icon | Icon Success (✓ xanh) | | | | Góc trên bên trái, cạnh tiêu đề. |
| 2 | Tiêu đề popup | Label (bold) | "Xác nhận phê duyệt" | | | |
| 3 | Mô tả | Label | Dynamic | | | Nội dung: "Bạn có chắc chắn phê duyệt báo cáo [Mã BC] và gửi lên [Tên đơn vị đích] không? Hành động này không thể hoàn tác." |
| 4 | Hủy | Button Outline | | | | Đóng popup, không thực hiện hành động. |
| 5 | Phê duyệt & Gửi | Button Success (xanh lá) | | | | Thực hiện phê duyệt và gửi báo cáo lên đơn vị đích. |
| 6 | Icon Đóng (✕) | Icon button | | | | Góc trên bên phải. Tương đương nhấn [Hủy]. |

**Popup Yêu cầu chỉnh sửa:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Icon | Icon Warning (⚠ vàng) | | | | Góc trên bên trái, cạnh tiêu đề. |
| 2 | Tiêu đề popup | Label (bold) | "Yêu cầu chỉnh sửa" | | | |
| 3 | Mô tả | Label | Dynamic | | | Nội dung: "Yêu cầu chỉnh sửa Báo cáo [Mã BC] với lý do đã nêu." |
| 4 | Lý do | Textarea | Null | x | x | Bắt buộc nhập. Max 3000 ký tự. Placeholder: "Nhập lý do yêu cầu chỉnh sửa". Auto-trim khoảng trắng đầu/cuối. Chỉ nhập khoảng trắng = rỗng (không hợp lệ). Nếu để trống hoặc chỉ khoảng trắng → hiển thị lỗi inline màu đỏ: *"Vui lòng nhập Lý do"*. Lỗi tự biến mất khi nhập dữ liệu hợp lệ. Tham chiếu: CMR_06, CMR_18. |
| 5 | Hủy | Button Outline | | | | Đóng popup, không thực hiện hành động. Dữ liệu đã nhập trong popup bị hủy. |
| 6 | Gửi yêu cầu chỉnh sửa | Button Warning (cam) | | | | Thực hiện gửi yêu cầu chỉnh sửa. **Disabled** khi trường "Lý do" trống hoặc chỉ chứa khoảng trắng. **Enabled** khi có ít nhất 1 ký tự hợp lệ. |
| 7 | Icon Đóng (✕) | Icon button | | | | Góc trên bên phải. Tương đương nhấn [Hủy]. |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý hành động Phê duyệt (Chỉ Đơn vị trung gian phê duyệt):**

- Trigger: User (đơn vị trung gian) nhấn [Phê duyệt] tại màn hình chi tiết.
- Popup "Xác nhận phê duyệt" hiển thị với mô tả: "Bạn có chắc chắn phê duyệt báo cáo [Mã BC] và gửi lên [Tên đơn vị đích] không? Hành động này không thể hoàn tác."
- Nhấn [Phê duyệt & Gửi]:
  - Trạng thái chuyển thành **"Đã tiếp nhận"** (final state — không thể thay đổi).
  - Hệ thống gửi thông báo in-app + email cho NĐT/Địa phương: "Báo cáo [Mã BC] đã được phê duyệt".
  - Card "Đã tiếp nhận" +1, card "Chờ duyệt" (hoặc YCCS) -1.
  - Toast T09 *"Đã phê duyệt báo cáo thành công"*.
  - Ẩn các nút hành động (YCCS/Phê duyệt) trên bản ghi.
- Thất bại (lỗi API): Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"* Popup đóng. Trạng thái giữ nguyên. Không auto-retry.
- Nhấn [Hủy] hoặc [✕]: Đóng popup, không thay đổi gì.

**Xử lý hành động Yêu cầu chỉnh sửa (YCCS) (Cả 2 loại đơn vị):**

- Trigger: User nhấn [Yêu cầu chỉnh sửa] tại màn hình chi tiết.
- Popup "Yêu cầu chỉnh sửa" hiển thị với mô tả: "Yêu cầu chỉnh sửa Báo cáo [Mã BC] với lý do đã nêu." User nhập lý do (bắt buộc, max 3000 ký tự, placeholder: "Nhập lý do yêu cầu chỉnh sửa").
- Nhấn [Gửi yêu cầu chỉnh sửa]:
  - Trạng thái chuyển thành **"Yêu cầu chỉnh sửa"**.
  - Hệ thống gửi thông báo in-app + email cho NĐT/Địa phương kèm lý do yêu cầu chỉnh sửa.
  - Form báo cáo phía NĐT/Địa phương được Enable cho phép chỉnh sửa và nộp lại.
  - Card "YCCS" +1 (nếu từ Chờ duyệt) hoặc giữ nguyên (nếu đã ở YCCS).
  - Toast T11 *"Đã gửi yêu cầu chỉnh sửa thành công"*.
  - Các nút hành động vẫn hiển thị (User có thể tiếp tục Phê duyệt sau đó nếu là đơn vị trung gian).
- Thất bại (lỗi API): Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"* Popup đóng. Trạng thái giữ nguyên. Không auto-retry.
- Nhấn [Hủy] hoặc [✕]: Đóng popup, không thay đổi gì.

**Xử lý hành động Chỉnh sửa (Chỉ Đơn vị đích nhận):**

- Trigger: User (đơn vị đích nhận) nhấn [Chỉnh sửa] tại màn hình chi tiết (khi TT = Đã tiếp nhận).
- Hệ thống chuyển sang chế độ chỉnh sửa: các trường dữ liệu được Enable cho phép đơn vị đích tự chỉnh sửa nội dung báo cáo.
- Sau khi chỉnh sửa xong, User nhấn [Lưu] để lưu thay đổi.

**Xử lý NĐT/Địa phương nộp lại (Luồng liên quan):**

- Khi NĐT/Địa phương chỉnh sửa và nộp lại báo cáo đã bị YCCS:
  - NĐT/Địa phương nhấn [Nộp] → Popup xác nhận hiển thị → Xác nhận.
  - Trạng thái chuyển về **"Chờ duyệt"**.
  - User nhận thông báo in-app + email: "Báo cáo [Mã BC] đã được nộp lại bởi [Tên NĐT/Cơ quan]".
  - Card "Chờ duyệt" +1, card "YCCS" -1.

**Xử lý Xem trước:**

- Trigger: Nút [Xem trước] tại bottom bar chi tiết.
- Logic: Tham chiếu CF_01. Mở popup preview PDF read-only.

**Xử lý Xuất báo cáo:**

- Trigger: Nút [Export] tại danh sách hoặc bottom bar chi tiết.
- Logic: Tham chiếu CF_04. Kết xuất biểu mẫu hiện tại ra file .docx hoặc .xlsx.
- Thành công: Toast — Tiêu đề: *"Thành công"*, Nội dung: *"Đã xuất báo cáo thành công"*.
- Thất bại: Toast — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"*

**Xử lý Xem vòng đời:**

- Trigger: Nút [Xem vòng đời báo cáo] tại bottom bar chi tiết hoặc icon trên danh sách.
- Logic: Tham chiếu CF_06. Mở popup timeline hiển thị lịch sử thao tác.

**Xử lý xung đột trạng thái (Race Condition):**

- Khi User nhấn [Đồng ý] trên popup nhưng trạng thái báo cáo đã bị thay đổi bởi process khác (VD: NĐT/Địa phương vừa nộp lại cùng lúc):
  - Hệ thống kiểm tra trạng thái hiện tại (server-side check) trước khi thực hiện action.
  - Nếu trạng thái không còn hợp lệ cho action đó → Toast lỗi T12 *"Trạng thái báo cáo đã thay đổi. Vui lòng tải lại trang"*
  - Popup đóng. Grid tự động reload để hiển thị trạng thái mới.

---

## Yêu cầu phi chức năng (NFR)

| Hạng mục | Yêu cầu |
| --- | --- |
| Performance | Thời gian load danh sách ≤ 3 giây. Thời gian phản hồi filter/search ≤ 1 giây. Thời gian xuất báo cáo file ≤ 5 giây. Thời gian xuất Excel ≤ 10 giây. |
| Concurrency | Giả định chỉ có 1 User xử lý trên mỗi cơ quan (không cần lock phức tạp). |
| Browser Compatibility | Chrome, Edge, Safari phiên bản mới nhất. |
| Notification | Thông báo in-app realtime. Email gửi async (không block UI). Template email: Pending thiết kế. |

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-15 | 1.0 | Khởi tạo | — | Tạo mới UC367-369 | Init Report Flow |
| 2026-05-15 | 1.0 → 1.1 | Bổ sung Scope, Preconditions, Postconditions | (Không có) | Thêm section Phạm vi + Điều kiện tiên quyết & Hậu điều kiện | BA confirm Q12, Q13 |
| 2026-05-15 | 1.0 → 1.1 | Empty State chi tiết | 1 empty state chung | 2 empty states: A (chưa có BC) + B (filter không kết quả) | BA confirm Q12 |
| 2026-05-15 | 1.0 → 1.1 | UC367-369.2 — Clarify read-only | "Tất cả trường Disabled" | Bổ sung: không validation rule, fields tùy thuộc biểu mẫu | BA confirm Q14 |
| 2026-05-15 | 1.0 → 1.1 | Error Handling cho actions | (Không có) | Thêm error handling (Toast lỗi) cho Phê duyệt/YCCS | BA confirm Q15 |
| 2026-05-15 | 1.0 → 1.1 | Race Condition handling | (Không có) | Server-side check trạng thái + Toast "Trạng thái đã thay đổi" + auto-reload | BA confirm Q16 |
| 2026-05-15 | 1.1 → 1.2 | Đổi tên UC367-369 → UC367-372 | UC367-369: Quản lý báo cáo NĐT đã nộp | UC367-372: Quản lý báo cáo NĐT/Địa phương nộp. Mở rộng scope bao gồm UC370-372 cho Địa phương. | Gộp NĐT + Địa phương vào cùng 1 UC |
| 2026-05-17 | CMR v2.0 | Thêm tham chiếu CMR_16, CMR_18 | Chưa có | Thêm CMR_16, CMR_18 trên các dòng filter/textarea | Filter dropdown phải có option Tất cả |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages | Trường bắt buộc | "Vui lòng nhập/chọn [tên trường]" | Đồng bộ CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04b Search placeholder fix | Tìm kiếm theo... | "Tìm kiếm nhanh theo mã báo cáo, tên báo cáo" | Chuẩn hóa CMR_06 STD-04b |
| 2026-05-18 | CMR v2.0 → 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-07 | 1.2 → 1.3 | Bỏ Tabs NĐT/Địa phương | 2 Tab: Nhà đầu tư / Địa phương | Gộp chung 1 danh sách, không phân biệt | Theo mockup mới |
| 2026-05-07 | 1.2 → 1.3 | Summary Cards 5 → 4 | 5 cards (Tổng, Đang xử lý, Đã tiếp nhận, YCCS, Từ chối) | 4 cards (Tổng đã nhận, Chờ duyệt, YCCS, Đã tiếp nhận) | Bỏ Từ chối, đổi tên Đang xử lý → Chờ duyệt |
| 2026-05-07 | 1.2 → 1.3 | Bỏ trạng thái Từ chối | Có trạng thái Từ chối + action Từ chối | Bỏ hoàn toàn trạng thái và action Từ chối | Theo yêu cầu BA |
| 2026-05-07 | 1.2 → 1.3 | Bộ lọc mới | Search + Ngày nộp (dropdown) + Trạng thái | Search + Phân hệ + Trạng thái + Đơn vị nộp + Ngày nộp (date-range) + Xuất Excel | Theo mockup mới |
| 2026-05-07 | 1.2 → 1.3 | Cột bảng mới | STT, Mã BC, Tên BC, Dự án, Đối tượng nộp, Ngày nộp, TT, Thao tác | STT, Mã BC, Tên BC, Phân hệ, Kỳ báo cáo, Đơn vị nộp, Ngày nộp, TT, Thao tác | Bỏ Dự án, thêm Phân hệ + Kỳ BC, đổi tên cột |
| 2026-05-07 | 1.2 → 1.3 | Cột Thao tác | Duyệt/Từ chối/YCCS/Xem/Export | Xem chi tiết, Xem vòng đời, Chỉnh sửa (Đã tiếp nhận), In, Export | Bỏ action trực tiếp trên danh sách |
| 2026-05-07 | 1.2 → 1.3 | Action buttons theo loại đơn vị | Chung cho tất cả Admin | Phân quyền: Đơn vị trung gian (YCCS + Phê duyệt) vs Đơn vị đích (YCCS + Chỉnh sửa) | Theo yêu cầu BA |
| 2026-05-07 | 1.2 → 1.3 | Thêm nút Xem trước | Không có | Thêm nút Xem trước (CF_01 preview PDF) tại bottom bar chi tiết | Theo mockup mới |
| 2026-05-07 | 1.2 → 1.3 | Mặc định hiển thị | Hiển thị tất cả trạng thái | Mặc định hiển thị báo cáo Chờ duyệt | Theo yêu cầu BA |
| 2026-05-07 | 1.2 → 1.3 | Đơn vị nộp logic | Tên NĐT / Tên Cơ quan (theo tab) | Tên đơn vị cụ thể; nếu cá nhân NĐT → full name cá nhân | Theo yêu cầu BA |
| 2026-05-07 | 1.3 → 1.4 | Clarify mô tả chức năng | Xem báo cáo NĐT/Địa phương nộp | Quản lý báo cáo mà đơn vị user login là trung gian/đích trong luồng phê duyệt. BC nộp bởi NĐT/TCKT/Địa phương | Comment review |
| 2026-05-07 | 1.3 → 1.4 | Bỏ Lưu ý Preconditions | Có dòng Lưu ý về Empty State | Xóa dòng Lưu ý (không liên quan) | Comment review |
| 2026-05-07 | 1.3 → 1.4 | Đơn vị nộp thêm VD TCKT | Chỉ VD địa phương + cá nhân | Thêm VD tổ chức kinh tế: "Công ty TNHH ABC", "Công ty CP XYZ" | Comment review |
| 2026-05-07 | 1.3 → 1.4 | Popup Phê duyệt/YCCS tách riêng | 1 popup chung, nút [Đồng ý] | Phê duyệt: popup xác nhận (không textarea), nút [Phê duyệt & Gửi]. YCCS: popup có textarea lý do, nút [Gửi yêu cầu chỉnh sửa] | Theo mockup mới |
