# LOGIC MÀN HÌNH CHUNG (COMMON SCREEN LOGIC - CS)

## Phân hệ Báo cáo | Hệ thống MBFS

> Tài liệu này định nghĩa các quy tắc chung về giao diện và thao tác cho các màn hình tiêu chuẩn trong hệ thống.

---

## CS_01: Cấu trúc Màn hình Danh sách chung (Common Listing Screen Structure)

### 1. Header

- **Báo cáo lẻ:** Header hiển thị tên báo cáo.
- **Báo cáo theo bộ hồ sơ (báo cáo gộp):** Header hiển thị **"Quản lý báo cáo + [Tên danh mục báo cáo]"**. VD: *Quản lý báo cáo xúc tiến đầu tư*.

### 2. Bộ lọc (Filters) - General Logic

- **Bắt buộc chung:** Mọi màn hình danh sách báo cáo bắt buộc phải có ít nhất 2 filter: **Trạng thái báo cáo** và **Tìm kiếm (Search bar)**.
- **Báo cáo định kỳ (Periodic):** Bắt buộc có filter **Năm** và **Trạng thái kỳ hạn**. Các filter khác (Quý, Tháng, Lĩnh vực...) bổ sung tùy đặc thù biểu mẫu.
- **Báo cáo không định kỳ:** **Không có** filter **Trạng thái kỳ hạn**.
- **Multiple Dropdown:** Tất cả các bộ lọc cho phép chọn nhiều giá trị bắt buộc phải sử dụng định dạng Checkbox bên trong dropdown.
- **Yearpicker:** Đối với các trường yêu cầu chọn Năm, sử dụng component YearPicker (chỉ cho phép chọn năm, không chọn ngày/tháng).
  - **Enable toàn bộ:** Tất cả các năm đều được Enable — người dùng có thể chọn bất kỳ năm nào, không phân biệt có hay không có dữ liệu.
  - **Empty State khi không có data:** Nếu người dùng chọn một năm không có dữ liệu báo cáo, danh sách hiển thị trạng thái **"Không có dữ liệu"** kèm hình ảnh minh họa (placeholder). Hệ thống không disable năm.
- **Kết hợp & Tự động lọc:** Có khả năng kết hợp đồng thời với thanh tìm kiếm (Search bar). Không cần nút xác nhận (button submit); hệ thống tự động lọc dữ liệu ngay khi người dùng chọn/thay đổi giá trị filter.

### 3. Thanh tìm kiếm (Search Bar)

- **Placeholder Text:** Hiển thị theo định dạng chuẩn: *"Tìm kiếm nhanh theo mã báo cáo"*.
- **Search Execution:** Không cần nhấn phím Enter. Dữ liệu tự động lọc ngay khi người dùng nhập ký tự. Áp dụng quy tắc **Debounce time (300ms - 500ms)** sau khi người dùng ngừng gõ để tránh gọi API liên tục.
- **Combination:** Có khả năng kết hợp đồng thời với các bộ lọc (Filters) để thu hẹp phạm vi kết quả.
- **Empty State:** Khi không có dữ liệu phù hợp với kết quả tìm kiếm/lọc, hiển thị thông báo *"Không tìm thấy dữ liệu phù hợp"* kèm hình ảnh minh họa (placeholder).

### 4. Hiển thị danh sách theo Kỳ hạn (Periodic Reporting)

- **Default State:** Tất cả các kỳ hạn báo cáo mặc định ở trạng thái Thu gọn (Collapse). Người dùng click vào header của kỳ hạn để Mở rộng (Expand).
- **Empty States Logic (Trạng thái dữ liệu trống):**
  - *Kỳ hạn chưa tới:* Hiển thị thông báo: *"Kỳ báo cáo này chưa tới hạn. Vui lòng đợi đến thời hạn để lập báo cáo"*.
  - *Trong kỳ hạn nhưng chưa có báo cáo:* Hiển thị thông báo: *"Chưa có báo cáo nào cho kỳ này. Nhấn 'Lập báo cáo' ở trên để tạo báo cáo mới"*.
  - *Qua kỳ hạn và chưa có báo cáo:* Hiển thị thông báo: *"Chưa có báo cáo nào cho kỳ này. Không thể tạo thêm."*
- **Giới hạn Nhập từ file sau kỳ hạn:** Không cho người dùng nhập từ file báo cáo mới sau khi hết kỳ hạn.
- **Record Limit per Period (Giới hạn bản ghi mỗi kỳ):** Hiển thị tối đa 10 bản ghi trong mỗi kỳ hạn. Nếu vượt quá 10 bản ghi, hệ thống kích hoạt thanh cuộn dọc (Scroll) bên trong riêng kỳ hạn đó.

### 5. Mô tả danh sách báo cáo (Phạm vi hiển thị cho Nhà Đầu Tư)

- **Quy tắc hiển thị dữ liệu:**
  - Danh sách hiển thị toàn bộ các báo cáo do chính Nhà đầu tư (NĐT) đang đăng nhập đã lập.
  - Ngoài ra, hệ thống cũng hiển thị các báo cáo thuộc các dự án mà NĐT có tham gia, bao gồm: báo cáo do **Tổ chức kinh tế (TCKT)** lập, hoặc báo cáo do một **NĐT khác** (cùng dự án) lập.
- **Hiển thị Biểu tượng (Icon Information) và Tooltip:**
  - Nhằm giúp NĐT phân biệt rõ nguồn gốc báo cáo, đối với các bản ghi **không phải do chính NĐT hiện tại lập** (tức là do TCKT hoặc NĐT khác lập), hệ thống sẽ hiển thị một biểu tượng Information (ℹ️) bên cạnh bản ghi trên danh sách.
  - Khi người dùng hover (di chuột) vào biểu tượng ℹ️ này, hệ thống sẽ hiển thị Tooltip cung cấp thông tin người lập thực tế:
    - Nếu báo cáo do TCKT lập: Tooltip hiển thị *"Báo cáo được lập bởi [Tên TCKT]"*.
    - Nếu báo cáo do NĐT khác lập: Tooltip hiển thị *"Báo cáo được lập bởi NĐT [Tên NĐT khác]"*.

---

## CS_02: Cấu trúc Màn hình Danh sách — Báo cáo Không Định kỳ

> Áp dụng cho tất cả báo cáo có Loại báo cáo = **Không định kỳ.**

### 1. Cấu trúc danh sách

- **Hiển thị phẳng:** Danh sách hiển thị các báo cáo không nhóm theo kỳ hạn. Hiển thị tối đa 10 bản ghi; nếu vượt quá 10 bản ghi, hệ thống kích hoạt thanh cuộn dọc (Scroll) để xem tiếp dữ liệu.
- **Nút [Tạo mới]:** Hiển thị trực tiếp trên header màn hình Danh sách. Không phụ thuộc vào kỳ hạn — Tất cả trạng thái.
- **Sắp xếp mặc định:** Theo Ngày cập nhật giảm dần (mới nhất lên trên).

### 2. Bộ lọc bắt buộc

| Filter                  | Bắt buộc      | Ghi chú                                                                                                                                                                                                                                                                                                                |
| ----------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trạng thái báo cáo  | ✓              | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Tham chiếu: CMR_03.                                                                                                                                                                                                                               |
| Tìm kiếm (Search bar) | ✓              | Tìm theo Mã báo cáo. Áp dụng quy tắc Debounce time (300ms - 500ms). Hiển thị Empty State *"Không tìm thấy dữ liệu phù hợp"* kèm placeholder khi không có kết quả. Tham chiếu: CMR_06, CMR_09.                                                                                                                                                                                                                                                                   |
| Năm                    | Tùy biểu mẫu | Nếu có:**Mặc định lọc theo năm của Ngày cập nhật bản ghi gần nhất.** Trường hợp biểu mẫu có trường ngày đặc thù và BA xác nhận rõ (VD: Ngày chấm dứt hoạt động, Năm tài chính) → lọc theo trường đó thay thế, ghi chú rõ trong SRS từng UC. Tham chiếu: CMR_07. |
| Dự án / Phạm vi      | Tùy biểu mẫu | Nếu báo cáo có Phạm vi báo cáo (chọn dự án). Tham chiếu: CMR_07.                                                                                                                                                                                                                                             |

---

## CS_03: Cấu trúc Màn hình Tổng hợp Báo cáo theo Phân hệ

> Áp dụng cho màn hình danh sách tổng hợp báo cáo. Màn hình này thay đổi cách hiển thị phụ thuộc vào phạm vi quyền hạn (số lượng phân hệ) mà người dùng được phép quản lý.

### 1. Phân quyền hiển thị và Cấu trúc Danh sách

- **Trường hợp User chỉ có quyền quản lý 1 phân hệ:**

  - **Giao diện:** Hiển thị dạng danh sách phẳng (Flat list).
  - **Bộ lọc Phân hệ:** Không hiển thị dropdown lọc "Phân hệ báo cáo".
  - **Mô tả:** Danh sách những báo cáo mà User từng được assign trong kỳ báo cáo được hiển thị trực tiếp bên dưới thanh tìm kiếm.
- **Trường hợp User có quyền quản lý nhiều phân hệ:**

  - **Giao diện:** Hiển thị danh sách dạng nhóm (Accordion / Grouped list).
  - **Bộ lọc Phân hệ:** Hiển thị dropdown bộ lọc "Phân hệ báo cáo" cạnh thanh tìm kiếm.
  - **Mô tả:** Các báo cáo được nhóm theo từng phân hệ trong các khung Accordion riêng biệt (VD: Xúc tiến đầu tư PROM, Đầu tư tại Việt Nam FDI...).
  - **Trạng thái mặc định:** Tất cả các Accordion mặc định ở trạng thái Thu gọn (Collapse).
  - **Giới hạn hiển thị trong Accordion:** Khi người dùng mở rộng (Expand) một Accordion, hiển thị tối đa 10 bản ghi bên trong. Nếu vượt quá 10 bản ghi, hệ thống sẽ kích hoạt thanh cuộn dọc (Scroll) bên trong riêng Accordion đó (không dùng phân trang).

### 2. Bộ lọc và Tìm kiếm

- **Bộ lọc Phân hệ báo cáo (Dropdown):**
  - **Định dạng:** Multiple choice (Cho phép chọn nhiều giá trị cùng lúc).
  - **Điều kiện hiển thị:** Chỉ xuất hiện khi người dùng có quyền trên 2 phân hệ trở lên.
- **Thanh tìm kiếm (Search Bar):**
  - **Placeholder:** *"Tìm kiếm nhanh theo tên báo cáo"* Tham chiếu: CMR_06.
  - **Thực thi:** Dữ liệu tự động lọc (real-time) ngay khi người dùng nhập từ khóa. Áp dụng quy tắc **Debounce time (300ms - 500ms)** sau khi người dùng ngừng gõ.
  - **Hành vi ẩn/hiện nhóm (khi áp dụng trên giao diện nhiều phân hệ):** Khi nhập từ khóa tìm kiếm, nếu trong một Accordion (phân hệ) không có báo cáo nào khớp với kết quả tìm kiếm, toàn bộ Accordion của phân hệ đó sẽ tự động **Ẩn đi**.
  - **Empty State:** Nếu không có báo cáo nào khớp trên toàn bộ các phân hệ, hiển thị thông báo *"Không tìm thấy dữ liệu phù hợp"* kèm hình ảnh minh họa (placeholder).

### 3. Quy tắc UI/UX khác

- Mỗi thẻ báo cáo trong danh sách hiển thị tên báo cáo, chu kỳ báo cáo (VD: "Kỳ báo cáo: Năm"), đi kèm biểu tượng tài liệu ở đầu và dấu mũi tên (chevron) ở cuối thẻ để điều hướng vào chi tiết.
- Các Header Accordion (đối với giao diện nhiều phân hệ) có màu nhấn (VD: đỏ đô) và có kèm mũi tên (chevron) ở góc phải để người dùng click Expand/Collapse.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật            | Before                                                       | After                                                                                                    | Ghi chú                              |
| ---------- | ----------- | -------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 2026-05-03 | 1.0 → 1.1  | CS_01                      | Trạng thái: Lưu nháp / Đã nộp / Yêu cầu chỉnh sửa | Trạng thái: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa                        | Cập nhật theo bộ trạng thái mới |
| 2026-05-08 | 1.1 → 1.2  | CS_01 Mục 2 — Yearpicker | Chỉ mô tả component, không có rule Enable/Disable       | Bổ sung: Enable chỉ các năm có data đã nộp hoặc năm tài chính hiện tại, còn lại Disabled | Yêu cầu mới                        |
| 2026-05-08 | 1.1 → 1.2  | CS_02 — Label + Filter    | Ngày cập nhật, Ngày cập nhật                           | Ngày cập nhật                                                                                         | Thống nhất tên cột                |
| 2026-05-08 | 1.2 → 1.3  | Thêm CS_03                | -                                                            | Thêm mới cấu trúc màn hình Tổng hợp Báo cáo theo Phân hệ                                     | Bổ sung logic UI/UX                  |
| 2026-05-11 | 1.3 → 1.4  | CS_01 — Thanh tìm kiếm    | Dữ liệu tự động lọc ngay khi người dùng nhập ký tự. Placeholder "Tìm kiếm theo [Giá trị tìm kiếm]" | Áp dụng Debounce 300-500ms, Placeholder "Tìm kiếm theo Mã báo cáo", thêm Empty State.                 | Tối ưu NFRs & UX                     |
| 2026-05-11 | 1.3 → 1.4  | CS_02 — Phân trang & Tìm kiếm | CMR_10 (phân trang theo bản ghi). Tìm theo Mã báo cáo.       | Dùng Scroll dọc nếu >10 bản ghi. Bổ sung Debounce & Empty State.                                         | Đồng bộ rule Scroll với CS_01        |
| 2026-05-11 | 1.3 → 1.4  | CS_03 — Phân trang & Tìm kiếm | Phân trang (Pagination) trong Accordion nếu > 10 bản ghi.    | Dùng Scroll dọc nếu >10 bản ghi. Bổ sung Debounce & Empty State cho toàn màn hình.                    | Đồng bộ rule Scroll với CS_01        |
| 2026-05-17 | 1.4 -> 1.5 | CS_01/CS_03 Search placeholder + CS_02 CMR_16 ref | Placeholder: Tim kiem theo... | Placeholder: Tim kiem nhanh theo... (CMR_06). Them CMR_16 vao filter Trang thai (CS_02). | Dong bo CMR v2.0 |
| 2026-05-18 | 1.5 -> 1.6 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.6 -> 1.7 | CS_01 Mục 2 — Yearpicker Enable/Disable | Enable chỉ năm có data hoặc năm tài chính hiện tại; các năm khác Disabled (hiển thị mờ, không cho chọn) | Enable toàn bộ tất cả các năm; nếu năm không có data → hiển thị Empty State "Không có dữ liệu", không Disabled năm | Thay đổi UX: bỏ logic disable năm theo yêu cầu |
| 2026-05-20 | 1.7 -> 1.8 | CS_03 Mục 1 — Mô tả danh sách (1 phân hệ) | Danh sách các báo cáo thuộc phân hệ đó được hiển thị trực tiếp bên dưới thanh tìm kiếm | Danh sách những báo cáo mà User từng được assign trong kỳ báo cáo được hiển thị trực tiếp bên dưới thanh tìm kiếm | Làm rõ phạm vi dữ liệu hiển thị theo comment review |
