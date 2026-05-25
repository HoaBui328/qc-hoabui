# UC364-366: Quản lý báo cáo đã nộp của tôi

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | (Chưa xác định) |
| **Phân hệ** | Tất cả (Cross-phân hệ) |
| **Mẫu biểu** | N/A — Màn hình tổng hợp quản lý báo cáo đã nộp |
| **Loại báo cáo** | N/A (Áp dụng cho tất cả loại báo cáo đã nộp) |
| **Hình thức nộp** | N/A |
| **Phạm vi dữ liệu đầu vào** | Không |
| **Cơ quan nhận** | N/A |
| **Đối tượng lập** | Tất cả Nhà đầu tư / Tổ chức kinh tế đã từng nộp báo cáo |
| **Giao diện** | User site (Phía người dùng) |
| **Ngày tạo** | 2026-05-15 |
| **Phiên bản** | 2.3 |

---

## Phạm vi (Scope)

### In Scope
- UC364-366.1: Xem danh sách báo cáo đã nộp + Lọc (Search, Filter Phân hệ, Filter Trạng thái, Filter Ngày nộp)
- UC364-366.2: Xem chi tiết báo cáo đã nộp (Full-page read-only, CF_07)
- UC364-366.3: Chỉnh sửa báo cáo đã nộp + Các tác vụ bổ trợ (Xem vòng đời, In, Xuất báo cáo)
- 4 Summary Cards thống kê theo trạng thái
- Xuất Excel danh sách báo cáo
- Pagination 10/20/50/100

### Out of Scope
- Quy trình duyệt/tiếp nhận phía cơ quan (Admin site) — bao gồm nhập lý do từ chối (xem UC367-372)
- Tạo mới báo cáo (thuộc luồng Lập báo cáo — các UC riêng theo phân hệ)
- Nhập từ file báo cáo
- Quản lý trạng thái dự án

### Preconditions

1. Người dùng đã đăng nhập thành công vào hệ thống với tài khoản NĐT hoặc TCKT.
2. Người dùng thuộc dự án có báo cáo do NĐT/TCKT khác lập (để có data hiển thị). Nếu không có data gì → Empty State A.
3. Hệ thống có kết nối API để lấy danh sách báo cáo và trạng thái.

### Postconditions

| Sau khi hoàn thành... | Trạng thái hệ thống |
| --- | --- |
| Xem danh sách | Danh sách hiển thị đúng phạm vi dữ liệu (CS_01 Mục 5). Summary Cards auto-count chính xác. |
| Lọc/Tìm kiếm | Grid cập nhật real-time theo AND logic. Cards không đổi/ảnh hưởng bởi kết quả lọc. |
| Chỉnh sửa (từ trạng thái YC chỉnh sửa) | Nhấn [Chỉnh sửa] → điều hướng đến màn chỉnh sửa (CF_03). Sau khi user edit xong → nút [Nộp báo cáo] enable. User nhấn [Nộp báo cáo] → trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03). Lifecycle Log ghi nhận. |
| Xuất báo cáo (per row) | Auto-download file .xlsx/.docx (không popup xác nhận). Toast thành công/lỗi. Tham chiếu: CF_04. |
| Xuất Excel (danh sách) | Auto-download file .xlsx chứa các bản ghi thỏa mãn filter hiện tại. Toast thành công/lỗi. |
| In | Mở trực tiếp hộp thoại in của trình duyệt (Print dialog). Tham chiếu: CF_05. Khác với [Xem trước] (popup xem trước PDF trong app — CF_07.1). |

---

## UC364-366.1: Xem Danh Sách Báo Cáo Đã Nộp + Lọc

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo đã nộp của tôi
- Chức năng cho phép người dùng xem toàn bộ các báo cáo mà chính họ đã nộp thành công (cross-phân hệ), theo dõi trạng thái xử lý (Chờ duyệt / Yêu cầu chỉnh sửa / Đã tiếp nhận), và thực hiện lọc/tìm kiếm nhanh.

Phân quyền: Tất cả Nhà đầu tư / Tổ chức kinh tế đã đăng nhập hệ thống.

Truy cập chức năng: Menu chính → Báo cáo đã nộp của tôi

Chức năng đáp ứng usecase số: 364, 365, 366

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **SUMMARY CARDS** | | | | | | |
| 1 | Tổng đã nộp | Card (Integer) | Tổng tất cả trạng thái | | | Hiển thị tổng số báo cáo trong danh sách (Chờ duyệt + YC chỉnh sửa + Đã tiếp nhận). Auto-count dựa trên dữ liệu bảng thực tế. **Không thay đổi** khi user thao tác filter (Phân hệ / Ngày nộp / Search). Click → reset filter trạng thái, grid hiển thị tất cả. Dropdown Trạng thái = "Tất cả trạng thái". Active state: border-left đậm + font-weight bold. |
| 2 | Yêu cầu chỉnh sửa | Card (Integer) | Số báo cáo YC chỉnh sửa | | | Số báo cáo đang ở trạng thái "Yêu cầu chỉnh sửa". Auto-count. Hiển thị icon cảnh báo (⚠️) khi giá trị > 0. Click → grid lọc chỉ hiển thị YC chỉnh sửa. Dropdown Trạng thái tự động = "Yêu cầu chỉnh sửa". Active state: border-left đậm + font-weight bold. |
| 3 | Chờ duyệt | Card (Integer) | Số báo cáo Chờ duyệt | | | Số báo cáo đang ở trạng thái "Chờ duyệt". Auto-count. Click → grid lọc chỉ hiển thị Chờ duyệt. Dropdown Trạng thái tự động = "Chờ duyệt". Active state: border-left đậm + font-weight bold. |
| 4 | Đã tiếp nhận | Card (Integer) | Số báo cáo Đã tiếp nhận | | | Số báo cáo đang ở trạng thái "Đã tiếp nhận". Auto-count. Click → grid lọc chỉ hiển thị Đã tiếp nhận. Dropdown Trạng thái tự động = "Đã tiếp nhận". Active state: border-left đậm + font-weight bold. |
| **BỘ LỌC & TÌM KIẾM** | | | | | | |
| 5 | Tìm kiếm | Search bar | Null | x | | Placeholder: "Tìm kiếm nhanh theo mã hoặc tên báo cáo". Max 255 ký tự. Phạm vi tìm: Mã báo cáo + Tên báo cáo. Partial match, case-insensitive, live search (debounce 300-500ms). Không tìm thấy → hiển thị Empty State B. Tham chiếu: CMR_06. |
| 6 | Phân hệ | Single-selection Dropdown | Tất cả phân hệ | x | | Giá trị: Tất cả phân hệ / Xúc tiến đầu tư / Đầu tư nước ngoài vào VN / Đầu tư VN ra nước ngoài / KCN-Khu kinh tế / Đầu tư trong nước. Chọn → grid lọc ngay (real-time). Tham chiếu: CMR_07. |
| 7 | Trạng thái | Single-selection Dropdown | Yêu cầu chỉnh sửa | x | | Giá trị: Tất cả trạng thái / Chờ duyệt / Yêu cầu chỉnh sửa / Đã tiếp nhận. **Mặc định khi vào màn hình: "Yêu cầu chỉnh sửa"** → grid chỉ hiển thị báo cáo YC chỉnh sửa, card "Yêu cầu chỉnh sửa" ở trạng thái active. Đồng bộ 2 chiều với Summary Cards: click card → dropdown tự cập nhật; thay đổi dropdown → card active tự cập nhật. Tham chiếu: CMR_07. |
| 8 | Ngày nộp (Từ) | Datepicker | 01/01/[Năm hiện tại] | x | | Định dạng: dd/MM/yyyy. Lọc báo cáo có ngày nộp >= giá trị. Kết quả lọc hiển thị ngay khi thay đổi. Validate: Nếu "Từ ngày" > "Đến ngày" → lỗi inline màu đỏ: "Ngày bắt đầu không được lớn hơn ngày kết thúc". Grid không lọc cho đến khi sửa. Cho phép để trống → không giới hạn ngày bắt đầu. |
| 9 | Ngày nộp (Đến) | Datepicker | [Ngày hiện tại] | x | | Định dạng: dd/MM/yyyy. Lọc báo cáo có ngày nộp <= giá trị. Kết quả lọc hiển thị ngay khi thay đổi. **Giới hạn: không được chọn ngày lớn hơn ngày hiện tại (max = today).** Cho phép để trống → không giới hạn ngày kết thúc. |
| **NÚT HÀNH ĐỘNG** | | | | | | |
| 10 | Xuất Excel | Button Secondary (màu xanh lá) | | | | Nhấn → Xuất danh sách báo cáo thỏa mãn điều kiện filter hiện tại ra file .xlsx. Auto-download. Thành công → Toast "Đã xuất danh sách báo cáo thành công". Thất bại → Toast "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" Nếu không có bản ghi nào (Empty State B) → Disable nút hoặc Toast "Không có dữ liệu để xuất". |
| **BẢNG DỮ LIỆU (GRID)** | | | | | | |
| 11 | STT | Integer (auto) | Null | | | Đánh số tự động theo trang hiện tại. Trang 1: 1-10, Trang 2: 11-20... |
| 12 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo theo cấu trúc [Phân hệ]\_[Mã Biểu]\_[ID]. VD: FDI\_AIV5\_012. Tham chiếu: CMR_09. |
| 13 | Tên báo cáo | Label | Null | | | Hiển thị tên đầy đủ của báo cáo. Max-width 250px. Text vượt quá → cắt ngắn + ellipsis (...). Hover → tooltip hiển thị full text. **Tooltip nguồn gốc (chỉ áp dụng cho bản ghi không phải do chính user hiện tại lập):** Hiển thị icon ℹ️ cạnh tên báo cáo. Hover → Tooltip nội dung: "Người lập: [Tên TCKT/full name NĐT đã lập báo cáo]". Tham chiếu: CS_01 Mục 5. |
| 14 | Phân hệ | Tag/Badge màu | Null | | | Hiển thị tên đầy đủ phân hệ dạng tag màu. Giá trị: Xúc tiến đầu tư / Đầu tư nước ngoài vào VN / Đầu tư VN ra nước ngoài / KCN-Khu kinh tế / Đầu tư trong nước. |
| 15 | Kỳ báo cáo | Label | Null | | | Hiển thị kỳ báo cáo tương ứng loại báo cáo. Format: Báo cáo năm → "Năm 2026"; Báo cáo quý → "Quý 1 năm 2026"; Báo cáo tháng → "Tháng 2 năm 2026"; Báo cáo 6 tháng → "Kỳ I năm 2026". |
| 16 | Ngày nộp | Label | Null | | | Định dạng: dd/MM/yyyy. Hiển thị ngày nộp gần nhất (latest submission date). Nếu báo cáo nộp nhiều lần (Nộp → YC chỉnh sửa → Nộp lại) → lấy ngày nộp lần cuối. Hỗ trợ sort: icon sort (↓/↑) trên header. Mặc định: Descending (mới nhất lên đầu). Click header → toggle Asc ↔ Desc. Sort áp dụng trên toàn bộ dataset. |
| 17 | Trạng thái | Badge màu | Null | | | Chờ duyệt = badge vàng (dot vàng + text). YC chỉnh sửa = badge đỏ (dot đỏ + text). Đã tiếp nhận = badge xanh lá (dot xanh + text). **Tooltip (chỉ YC chỉnh sửa):** Hiển thị icon (i) bên cạnh badge. Nhấn/Hover → tooltip hiện lý do cấp trên yêu cầu chỉnh sửa báo cáo. Nội dung: Label "Lý do:" (bold) + body text lý do yêu cầu chỉnh sửa (lấy từ action YCCS của cấp trên tại UC367-372). Tooltip hiển thị toàn bộ nội dung (không cắt ngắn). Mouse rời icon → tooltip tự ẩn. |
| 18 | Thao tác | Button group | Null | | | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC364-366.3. |
| **PHÂN TRANG** | | | | | | |
| 19 | Phân trang | Pagination | 10 báo cáo/trang | | | Hiển thị text: "Hiển thị [start]-[end] / [total] báo cáo". Dropdown chọn số bản ghi/trang: 10 / 20 / 50 / 100. Button [Trang trước]: Disabled khi ở trang 1. Button [Trang sau]: Disabled khi ở trang cuối. Số trang: hiển thị nút số trang, trang hiện tại = active (highlight). Tham chiếu: CMR_10. |

---

### 3. Mô tả các xử lý của chức năng

- Phạm vi hiển thị dữ liệu:
  - Danh sách hiển thị các báo cáo mà **chính user hiện tại** đã lập, VÀ các báo cáo thuộc dự án mà user có tham gia (bao gồm báo cáo do TCKT lập hoặc NĐT khác cùng dự án lập). Tham chiếu: CS_01 Mục 5.
  - Dữ liệu cross-phân hệ: hiển thị báo cáo từ tất cả phân hệ mà user liên quan.
  - Đối với bản ghi không phải do user hiện tại lập: hiển thị icon ℹ️ cạnh Tên báo cáo + tooltip "Người lập: [Tên TCKT/full name NĐT]". Tham chiếu: CS_01 Mục 5.
  - **Logic NĐT thuộc dự án có TCKT đứng pháp danh:** Nếu user là Nhà đầu tư thuộc dự án có TCKT đứng pháp danh, các báo cáo do TCKT lập đều hiển thị trong danh sách của NĐT. Tuy nhiên NĐT **chỉ có quyền**: Xem chi tiết, Xem vòng đời, In, Export. **Không có action Chỉnh sửa** ở bất kỳ trạng thái nào.

- Logic Summary Cards:
  - 4 cards auto-count dựa trên dữ liệu bảng thực tế (disabled — user không thể chỉnh sửa giá trị).
  - Số liệu **không thay đổi** khi user thao tác filter (Phân hệ / Ngày nộp / Search) trong session hiện tại.
  - Đồng bộ 2 chiều với dropdown Trạng thái: user thay đổi dropdown → card active cập nhật tương ứng. User chọn "Tất cả trạng thái" → card "Tổng đã nộp" active.

- Logic bộ lọc:
  - Tất cả bộ lọc hoạt động đồng thời (AND logic). Grid chỉ hiển thị bản ghi thỏa mãn TẤT CẢ điều kiện filter đang active.
  - Search bar áp dụng Debounce 300-500ms sau khi người dùng ngừng gõ. Tham chiếu: CMR_06.
  - Dropdown Phân hệ và Trạng thái lọc ngay khi chọn (real-time). Tham chiếu: CMR_07.
  - Datepicker Ngày nộp: Validate "Từ ngày" > "Đến ngày" → hiển thị lỗi inline, grid không lọc cho đến khi sửa.

- Logic Xuất Excel:
  - Xuất danh sách báo cáo thỏa mãn điều kiện filter hiện tại (Phân hệ + Trạng thái + Ngày nộp + Search) ra file .xlsx.
  - File xuất bao gồm các cột: STT, Mã báo cáo, Tên báo cáo, Phân hệ, Kỳ báo cáo, Ngày nộp, Trạng thái, Lý do chỉnh sửa.
  - Cột "Lý do chỉnh sửa" (cạnh cột Trạng thái): Fill dữ liệu lý do chỉnh sửa khi báo cáo được action "Yêu cầu chỉnh sửa" từ cấp trên. Nếu báo cáo không ở trạng thái YCCS hoặc chưa từng bị YCCS → để trống.
  - Auto-download, không popup xác nhận.

- Empty States:
  - **Empty State A** (user chưa có báo cáo nào trong danh sách): Icon document xám. Tiêu đề: "Chưa có báo cáo nào được nộp". Mô tả: "Các báo cáo sau khi được nộp thành công sẽ hiển thị tại đây. Bạn có thể theo dõi trạng thái xử lý của từng báo cáo." Summary cards: Tất cả = 0.
  - **Empty State B** (search/filter không có kết quả): Icon search xám nhạt (centered). Tiêu đề: "Không tìm thấy kết quả" (font-weight bold, màu xám đậm). Layout: icon + tiêu đề căn giữa theo chiều dọc trong vùng grid.

- Sắp xếp mặc định: Theo Ngày nộp giảm dần (mới nhất lên đầu). Sort áp dụng trên toàn bộ dataset (không chỉ trang hiện tại).

- Trạng thái mặc định khi vào màn hình:
  - Dropdown Trạng thái = "Yêu cầu chỉnh sửa". Grid chỉ hiển thị các báo cáo ở trạng thái "Yêu cầu chỉnh sửa".
  - Card "Yêu cầu chỉnh sửa" ở trạng thái active (border-left đậm + font-weight bold).
  - User có thể chọn card khác hoặc đổi dropdown để xem các trạng thái khác.

---


## UC364-366.2: Xem Chi Tiết Báo Cáo Đã Nộp

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem chi tiết báo cáo đã nộp
- Chức năng cho phép người dùng xem toàn bộ nội dung báo cáo đã nộp ở chế độ read-only (full-page). Hiển thị đầy đủ dữ liệu đã nộp theo đúng biểu mẫu tương ứng.

Phân quyền: User đã nộp báo cáo (chính chủ).

Truy cập chức năng: Màn danh sách (UC364-366.1) → Cột Thao tác → Nhấn nút [Xem chi tiết]

Chức năng đáp ứng usecase số: 365

---

### 2. Mô tả giao diện

**Màn hình xem chi tiết (Full-page, Read-only)**

Tham chiếu: CF_07 (mở rộng — full-page mode).

---

### 3. Mô tả các xử lý của chức năng

- Nhấn [Xem chi tiết] → Hệ thống điều hướng đến màn hình xem chi tiết full-page (read-only). Đây là View Detail Screen — khác với Preview PDF (popup).
- Hiển thị toàn bộ dữ liệu báo cáo theo đúng biểu mẫu tương ứng. Tất cả trường ở trạng thái Disabled (không cho phép chỉnh sửa).
- Các nút hành động trên màn hình xem chi tiết: [Xem trước], [In], [Xuất báo cáo], [Quay lại].
  - [Xem trước]: Mở popup PDF Preview báo cáo. Tham chiếu: CF_07 (mục "Preview PDF").
  - [In]: Mở Print Preview PDF → hộp thoại in trình duyệt. Tham chiếu: CF_05.
  - [Xuất báo cáo]: Kết xuất file .xlsx hoặc .docx (tùy biểu mẫu). Tham chiếu: CF_04.
  - [Quay lại]: Điều hướng về màn hình Danh sách (UC364-366.1).

---


## UC364-366.3: Chỉnh Sửa Báo Cáo Đã Nộp + Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Chỉnh sửa báo cáo đã nộp và các tác vụ bổ trợ
- Chức năng cho phép người dùng chỉnh sửa báo cáo khi bị yêu cầu chỉnh sửa, cùng các tác vụ bổ trợ: Xem vòng đời, In, Xuất báo cáo.

Phân quyền:
- Case A (ĐTNN/ĐTTN — CMR_01): Chỉ TCKT phụ trách mới có quyền [Chỉnh sửa]. NĐT thành viên → Ẩn nút [Chỉnh sửa], chỉ có quyền Xem/In/Xuất báo cáo.
- Case B (ĐTRNN — CMR_02): Tất cả NĐT trong dự án đều có quyền [Chỉnh sửa] khi bản ghi ở trạng thái "Yêu cầu chỉnh sửa".
- **Case C (NĐT thuộc dự án có TCKT đứng pháp danh):** NĐT thấy báo cáo do TCKT lập trong danh sách, nhưng **chỉ có quyền**: Xem chi tiết, Xem vòng đời, In, Export. **Không có action Chỉnh sửa** ở bất kỳ trạng thái nào.

Truy cập chức năng: Màn danh sách (UC364-366.1) → Cột Thao tác → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 364, 366

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Chỉnh sửa | Button Primary | Chỉ "Yêu cầu chỉnh sửa" | Case A: Chỉ TCKT (CMR_01). Case B: Tất cả NĐT (CMR_02). Last Write Wins khi nhiều NĐT cùng sửa. | Nhấn → điều hướng đến màn chỉnh sửa báo cáo (CF_03). Sau khi user edit xong → nút [Nộp báo cáo] enable. |
| 2 | Xem chi tiết | Button Outline | Tất cả trạng thái | Tất cả user | Điều hướng đến màn hình View Detail Screen (full-page, read-only). Tham chiếu: CF_07 (full-page mode). |
| 3 | Xem vòng đời | Button Icon | Tất cả trạng thái | Tất cả user | Tham chiếu: CF_06. |
| 4 | In | Button Icon | Tất cả trạng thái | Tất cả user | Tham chiếu: CF_05. |
| 5 | Xuất báo cáo | Button Icon | Tất cả trạng thái | Tất cả user | Tham chiếu: CF_04. |

---

### 3. Mô tả các xử lý của chức năng

- Chỉnh sửa: Tham chiếu: CF_03. Áp dụng khi trạng thái = "Yêu cầu chỉnh sửa". Nhấn [Chỉnh sửa] → điều hướng đến màn chỉnh sửa. Sau khi user edit xong → nút [Nộp báo cáo] enable. User nhấn [Nộp báo cáo] → trạng thái chuyển theo CMR_03. Case B (ĐTRNN): Tất cả NĐT đều có quyền, áp dụng Last Write Wins (CMR_02).
- Xem chi tiết: Điều hướng đến màn hình View Detail Screen full-page (UC364-366.2). Tham chiếu: CF_07 (full-page mode).
- Xem vòng đời: Tham chiếu: CF_06.
- In: Mở Print Preview PDF → hộp thoại in trình duyệt. Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất file .xlsx hoặc .docx (tùy biểu mẫu). Auto-download. Thành công → Toast "Đã xuất báo cáo thành công". Thất bại → Toast "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" Tham chiếu: CF_04.

---


---

## Yêu cầu phi chức năng (NFR)

| Hạng mục | Yêu cầu |
| --- | --- |
| Performance | Thời gian load danh sách ≤ 3 giây. Thời gian phản hồi filter/search ≤ 1 giây. |
| Concurrency | Dữ liệu grid không real-time push. Cập nhật khi user reload/filter/navigate. |
| Browser Compatibility | Chrome, Edge, Safari phiên bản mới nhất. |
| Accessibility | Summary Cards hỗ trợ keyboard navigation. Badge trạng thái có aria-label. |

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-15 | 1.0 | Khởi tạo | — | Tạo mới UC364-366 | Init Report Flow |
| 2026-05-17 | CMR v2.0 | STD-04b Search placeholder fix (1) | Tim kiem theo... | Tim kiem nhanh theo ma hoac ten bao cao | Chuan hoa CMR_06 STD-04b |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-19 | 2.2 | Cập nhật theo mockup mới | 5 Summary Cards (có Lưu nháp), [Chỉnh sửa] cho Lưu nháp + YC chỉnh sửa, không có nút Xuất Excel, tooltip "Lý do từ chối:" | 4 Summary Cards (bỏ Lưu nháp), [Chỉnh sửa] chỉ cho YC chỉnh sửa, thêm nút Xuất Excel (export theo filter), tooltip "Lý do:" | Đồng bộ mockup + confirm BA |
| 2026-05-07 | 2.2 → 2.3 | Ngày nộp (Đến) giới hạn | Không giới hạn max | Max = ngày hiện tại (không cho chọn ngày tương lai) | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Bỏ nút Lập báo cáo | Có nút [+ Lập báo cáo] | Xóa nút, chỉ giữ [Xuất Excel] | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Phân hệ không viết tắt | Tên viết tắt: XTĐT / ĐTNN / ĐTRNN / KCN-KKT / ĐTTN | Tên đầy đủ: Xúc tiến đầu tư / Đầu tư nước ngoài vào VN / ... | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Tooltip YCCS clarify | Hover → tooltip hiện lý do | Nhấn/Hover → tooltip hiện lý do cấp trên yêu cầu chỉnh sửa (lấy từ UC367-372) | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Tooltip nguồn gốc → cạnh Tên BC | Row riêng #20, icon cạnh bản ghi | Gộp vào cột Tên báo cáo, icon ℹ️ cạnh tên, tooltip "Người lập: [Tên TCKT/NĐT]" | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Logic NĐT thuộc dự án có TCKT | Không có | NĐT thấy BC do TCKT lập nhưng chỉ Xem/Vòng đời/In/Export, không Chỉnh sửa | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Xuất Excel thêm cột | Không có cột Lý do chỉnh sửa | Thêm cột "Lý do chỉnh sửa" cạnh Trạng thái | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Empty State A bỏ nút | Có nút [+ Lập báo cáo] | Bỏ nút, chỉ hiển thị icon + tiêu đề + mô tả | Comment review |
| 2026-05-07 | 2.2 → 2.3 | Empty State B bỏ mô tả | Có mô tả "Thử thay đổi từ khóa..." | Bỏ mô tả, chỉ giữ icon + tiêu đề | Comment review |
