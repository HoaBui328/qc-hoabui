# UC095-100: Báo cáo tình hình điều chỉnh giấy chứng nhận đăng ký đầu tư/giấy tờ có giá trị tương đương cho nhà đầu tư nước ngoài trong lĩnh vực ... Quý ... (Mẫu A.IV.6)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.6 |
| **Loại báo cáo** | Định kỳ quý |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài) |
| **Đối tượng lập** | Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.5 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV6_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý:** Báo cáo được lập **riêng biệt bởi từng Bộ** (Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN). Mỗi Bộ gửi 1 bản độc lập theo lĩnh vực quản lý của mình. Phạm vi dữ liệu hiển thị theo CMR_02.
>
> **Phân quyền cách ly hoàn toàn:** Mỗi Bộ chỉ nhìn thấy và thao tác được báo cáo do Bộ mình lập. Bộ A không thể xem, chỉnh sửa, hoặc xóa báo cáo của Bộ B.
>
> **Phạm vi chức năng:** Ngoài các chức năng Lập báo cáo, Xem danh sách và Tác vụ bổ trợ, UC này còn bao gồm chức năng **Nhập từ file báo cáo** theo CF_02 Case 2 (không có Phạm vi). Chi tiết tham khảo UC089-094.
>
> **Ngoài phạm vi:** Quản lý master data dự án (thuộc phân hệ khác); Phê duyệt báo cáo (phía cơ quan nhận — Bộ Tài chính); Quy trình xử lý sau khi báo cáo được tiếp nhận.

---

## UC095-100.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình điều chỉnh GCNĐKĐT/giấy tờ tương đương cho NĐT nước ngoài theo lĩnh vực (Mẫu A.IV.6)
- Chức năng cho phép Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN truy cập danh sách báo cáo định kỳ quý, được nhóm theo từng Kỳ hạn báo cáo. Mỗi Bộ chỉ thấy báo cáo do Bộ mình lập.

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN. Phân quyền cách ly hoàn toàn — mỗi Bộ chỉ nhìn thấy báo cáo do Bộ mình lập. Tham chiếu: CMR_02.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo điều chỉnh GCNĐKĐT theo lĩnh vực (Mẫu A.IV.6)

Chức năng đáp ứng usecase số: 95, 96, 97, 98, 99, 100

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng nhấp để chọn năm. Hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay, không cần nhấn thêm nút. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Tất cả | x | | Lọc theo trạng thái kỳ hạn. Chọn một hoặc nhiều giá trị: Tất cả / Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả hiển thị ngay. Tham chiếu: CMR_04, CMR_07, CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn (VD: "Quý 1 Năm 2026"). Mặc định collapse; người dùng click để expand. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Trạng thái kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_01. |
| 8 | Nhập từ file | Button | Null | | | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_02 Case 2 (không có Phạm vi). Chi tiết luồng Nhập từ file tham khảo UC089-094. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh. Tham chiếu: CMR_09. |
| 11 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 12 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 13 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC095-100.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (theo quý), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (kỳ mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Các nút [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ chưa bắt đầu (Chưa tới hạn) và kỳ đã qua (Qua kỳ báo cáo). Tham chiếu: CF_01.
- Mỗi Bộ chỉ thấy báo cáo của Bộ mình — phân quyền cách ly hoàn toàn. Bộ A không thể xem, chỉnh sửa, hoặc xóa báo cáo của Bộ B. Tham chiếu: CMR_02.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức, không cần nhấn thêm nút.
- Phân trang. Tham chiếu: CMR_10.

---


## UC095-100.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo điều chỉnh GCNĐKĐT theo lĩnh vực (Mẫu A.IV.6)
- Chức năng cho phép từng Bộ ghi nhận thông tin điều chỉnh giấy chứng nhận đăng ký đầu tư. Mỗi dòng trong bảng đại diện cho 1 lần điều chỉnh của 1 dự án. Khi mở form, hệ thống tự động truy vấn DB và load sẵn các dòng dữ liệu điều chỉnh (dòng API) với C2→C9 được auto-fill. Ngoài ra, user có thể thêm dòng mới (dòng user) và nhập Mã số dự án (C2) thủ công — hệ thống kiểm tra sự tồn tại và tự động điền thông tin gốc (C3, C4) cùng số lần điều chỉnh hiện tại (C5).

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN. Phân quyền cách ly hoàn toàn. Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC095-100.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 95, 96

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Màn hình lập báo cáo theo biểu mẫu A.IV.6, gồm Phần Header và Bảng dữ liệu Dynamic Table.

> **Dynamic Table — 2 nguồn dữ liệu:**
> - **Dòng auto-load:** Khi mở form lập/chỉnh sửa báo cáo, hệ thống tự động truy vấn DB và load sẵn các dòng dữ liệu điều chỉnh của dự án trong quý đã chọn. Toàn bộ C2→C9 được hệ thống tự động điền. Tất cả cột vẫn **Editable** — user được phép hiệu chỉnh nếu cần. User chịu trách nhiệm cuối cùng về nội dung báo cáo.
> - **Dòng user thêm tay:** User nhấn [Thêm dòng] (B1) để thêm dòng trống. Tất cả trường **Enabled** — user nhập C2 thủ công, hệ thống tra cứu DB khi blur. Nếu C2 hợp lệ → auto-fill C3→C9, tất cả vẫn Editable.
> - Tất cả dòng đều cho phép sửa và xóa.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN HEADER** | | | | | | |
| 1 | Tên Bộ/Ngành | Label | Auto-fill | | | Hệ thống tự động điền theo tổ chức của user đang đăng nhập (VD: "BỘ TƯ PHÁP", "BỘ CÔNG THƯƠNG", "NGÂN HÀNG NHÀ NƯỚC VIỆT NAM"). Disabled. Tham chiếu: CMR_12. |
| 2 | Lĩnh vực báo cáo | Text input | Auto-suggest theo Bộ | x | x | **Text input bình thường** (không phải dropdown). Hệ thống gợi ý giá trị mặc định theo tổ chức đăng nhập: Bộ Công thương → "DẦU KHÍ"; Bộ Tư pháp → "CÔNG TY LUẬT"; Ngân hàng Nhà nước VN → "NGÂN HÀNG NƯỚC NGOÀI". Người dùng được phép thay đổi giá trị tự do. Giá trị này điền vào biến "TRONG LĨNH VỰC......" trên tiêu đề báo cáo và hiển thị tại cột Lĩnh vực trên màn hình danh sách. Tham chiếu: CMR_06. |
| 3 | Quý báo cáo | Dropdown | Quý hiện tại | | x | Hiển thị quý báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05. |
| 4 | Năm báo cáo | Yearpicker | Năm hiện tại | | x | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05. |
| **A. Nhóm thông tin Quyết định & Dự án** | | | | | | |
| C1 | STT | Label | Auto-fill | | | Hệ thống tự động điền số thứ tự tăng dần từ 1. Read-only, không cho phép chỉnh sửa. |
| C2 | Mã số dự án/ Số GCNĐT/ Số Giấy tờ có giá trị tương đương | Text | Null | x | x | Text free (không validate format ký tự). Tối đa 255 ký tự. **Dòng auto-load:** Hệ thống tự động điền từ DB, vẫn Editable. **Dòng user thêm tay:** Người dùng nhập mã số dự án hoặc số giấy phép. Placeholder: "Nhập mã số dự án hoặc số giấy phép". Hệ thống tự động trim khoảng trắng thừa đầu/cuối. Kiểm tra tồn tại: Khi người dùng nhập và rời khỏi ô, hệ thống tra cứu mã trong DB. Nếu mã chưa tồn tại → hiển thị cảnh báo inline: "Mã dự án này chưa được khởi tạo trên hệ thống. Vui lòng kiểm tra lại" và không thực hiện auto-fill. Nếu mã hợp lệ → hệ thống tự động điền C3→C9. **Khi user xóa hoặc sửa C2 sau khi đã auto-fill:** Hệ thống clear/reset toàn bộ C3→C9 về trạng thái ban đầu (trống). Tham chiếu: CMR_05, CMR_06, CMR_12. |
| C3 | Ngày cấp | Date | Từ hệ thống | x | x | Hệ thống tự động điền từ dữ liệu gốc của dự án sau khi C2 được xác minh hợp lệ. Vẫn Editable — user được phép hiệu chỉnh. Định dạng: dd/MM/yyyy. Tham chiếu: CMR_12. |
| C4 | Tên dự án / doanh nghiệp | Text | Từ hệ thống | x | x | Hệ thống tự động điền từ dữ liệu gốc của dự án sau khi C2 được xác minh hợp lệ. Vẫn Editable — user được phép hiệu chỉnh. Tham chiếu: CMR_12. |
| **B. Nhóm thông tin Điều chỉnh** | | | | | | |
| C5 | Lần điều chỉnh | Label | Từ hệ thống | | | Hệ thống tự động query lịch sử điều chỉnh của Mã số dự án (C2) trong DB, đếm tổng số lần đã điều chỉnh trước đó và hiển thị theo định dạng: "Lần thứ n" (n>0, nguyên dương). Trong cùng 1 báo cáo, nếu cùng mã GCNĐT xuất hiện ở nhiều dòng, giá trị n ở các dòng phải tăng dần và không được trùng nhau. Read-only. Disabled. Tham chiếu: CMR_12. |
| C6 | Ngày điều chỉnh | Date Picker | Null | x | x | Hệ thống auto-fill từ dữ liệu điều chỉnh của dự án, vẫn **Editable** — user được phép hiệu chỉnh. Validate 2 điều kiện: (1) C6 phải >= C3 (Ngày cấp); nếu vi phạm → lỗi inline: "Ngày điều chỉnh không được nhỏ hơn ngày cấp dự án" (2) C6 phải <= ngày hiện tại; nếu vi phạm → lỗi inline: "Không được chọn ngày ở tương lai" Tham chiếu: CMR_05, CMR_08. |
| C7 | Nội dung điều chỉnh cụ thể - Trước khi điều chỉnh | Textarea | Null | x | x | **Luôn Enabled** bất kể dòng API hay dòng user. Hệ thống hiển thị nội dung điều chỉnh (trước điều chỉnh) từ dữ liệu điều chỉnh của dự án trong quý đã chọn (mục "Nội dung cũ/Nội dung đã quy định tại..." từ hồ sơ đề nghị điều chỉnh). Cho phép user chỉnh sửa. Tối đa 3000 ký tự. Error maxlength: "[Tên trường] không được vượt quá 3000 ký tự". Error required: "Vui lòng nhập Nội dung điều chỉnh trước". Tham chiếu: CMR_05, CMR_06, CMR_08. Placeholder: "Nhập nội dung trước điều chỉnh". |
| C8 | Nội dung điều chỉnh cụ thể - Sau khi điều chỉnh | Textarea | Null | x | x | **Luôn Enabled** bất kể dòng API hay dòng user. Hệ thống hiển thị nội dung điều chỉnh (sau điều chỉnh) từ dữ liệu điều chỉnh của dự án trong quý đã chọn (mục "Nội dung mới/Nay đăng ký sửa thành..." từ hồ sơ đề nghị điều chỉnh). Cho phép user chỉnh sửa. Tối đa 3000 ký tự. Error maxlength: "[Tên trường] không được vượt quá 3000 ký tự". Error required: "Vui lòng nhập Nội dung điều chỉnh sau". Tham chiếu: CMR_05, CMR_06, CMR_08. Placeholder: "Nhập nội dung sau điều chỉnh". |
| C9 | Ghi chú | Text | Null | x | | **Luôn Enabled** bất kể dòng API hay dòng user. Không bắt buộc. Giới hạn tối đa **255 ký tự**; hiển thị bộ đếm ký tự còn lại. Hệ thống lấy dữ liệu từ mục "Lý do giải trình điều chỉnh" từ hồ sơ đề nghị điều chỉnh và hiển thị. Cho phép người dùng chỉnh sửa. Tham chiếu: CMR_06, CMR_08. |
| **Các Button** | | | | | | |
| B1 | Thêm dòng | Button | | | | Người dùng nhấn để thêm 1 **dòng user** mới vào cuối bảng. Dòng mới được khởi tạo trống, tất cả trường Enabled, STT tự động tăng. Icon Xóa dòng (B2) hiển thị cho dòng này. |
| B2 | Xóa dòng | Icon Button (mỗi dòng) | | | | Hiển thị trên tất cả dòng. Người dùng nhấn icon xóa tại dòng tương ứng. Hệ thống hiển thị popup xác nhận: "Bạn có chắc chắn muốn xóa dòng này?" với nút [Đồng ý] / [Hủy]. Sau khi xóa, STT các dòng còn lại được cập nhật lại. Tham chiếu: CMR_06. |
| B3 | Lưu nháp | Button | | | | **Luôn Enabled.** Lưu toàn bộ dữ liệu hiện tại ở trạng thái Lưu nháp mà không cần validate đầy đủ. Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | **Luôn Enabled.** Hệ thống validate toàn bộ trường bắt buộc và các ràng buộc logic cross-field (C6 vs C3, C7 vs C8) trước khi nộp. Nếu có lỗi → hiển thị lỗi inline tại trường tương ứng, không nộp. Tham chiếu: CF_01. |
| B1 | Hủy | Button | | | | Hủy bỏ thao tác và quay về màn hình Danh sách. Hiển thị popup xác nhận nếu đã có thay đổi chưa lưu. Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo Excel), CF_05 (In).

**Xử lý đặc thù biểu mẫu A.IV.6:**

- **Phân quyền theo Bộ:** Khi khởi tạo form, hệ thống xác định tổ chức của user đang đăng nhập để auto-fill Tên Bộ/Ngành và gợi ý Lĩnh vực mặc định. Mỗi Bộ chỉ xem và thao tác báo cáo của Bộ mình — cách ly hoàn toàn. Tham chiếu: CMR_02, CMR_12.
- **Auto-load dữ liệu:** Khi mở form lập/chỉnh sửa báo cáo, hệ thống tự động truy vấn DB và load sẵn các dòng dữ liệu điều chỉnh của dự án trong quý đã chọn. Toàn bộ C2→C9 được hệ thống tự động điền. Tất cả cột vẫn **Editable** — user được phép hiệu chỉnh nếu cần.
- **Kiểm tra tồn tại dự án (C2 — dòng user thêm tay):** Khi user nhập C2 và rời khỏi ô, hệ thống tra cứu mã trong DB. Nếu không tìm thấy → cảnh báo inline, không auto-fill. Nếu hợp lệ → auto-fill C3→C9, tất cả vẫn Editable. Tham chiếu: CMR_05, CMR_12.
- **Reset khi xóa/sửa C2:** Khi user xóa hoặc sửa giá trị C2 sau khi đã auto-fill, hệ thống clear/reset toàn bộ C3→C9 về trạng thái ban đầu (trống).
- **Auto-fill Lần điều chỉnh (C5):** Hệ thống query lịch sử điều chỉnh của mã dự án → đếm tổng lần đã điều chỉnh → C5 = Tổng cũ + 1. Hiển thị "Lần thứ N". Read-only. Tham chiếu: CMR_12.
- **Validate C6:** Kiểm tra C6 ≥ C3 và C6 ≤ ngày hiện tại. Hiển thị lỗi inline riêng cho từng vi phạm. Tham chiếu: CMR_05, CMR_08.
- **Validate C7 ≠ C8:** Hệ thống so sánh nội dung C7 và C8 sau khi trim. Nếu giống hệt → hiển thị lỗi inline tại C8: **"Nội dung trước và sau điều chỉnh không được giống nhau"**. Kiểm tra khi Nộp và khi blur khỏi C8. Tham chiếu: CMR_05.
- **Validate Required C7:** Khi Nộp, nếu C7 trống → hiển thị lỗi inline: **"Vui lòng nhập Nội dung điều chỉnh trước"**. Tham chiếu: CMR_06.
- **Validate Required C8:** Khi Nộp, nếu C8 trống → hiển thị lỗi inline: **"Vui lòng nhập Nội dung điều chỉnh sau"**. Tham chiếu: CMR_06.
- **Bộ đếm ký tự:** C7, C8 hiển thị số ký tự còn lại (tối đa 3000). C9 hiển thị số ký tự còn lại (tối đa 255). Tham chiếu: CMR_08.
- **Sort:** Các cột có giá trị ngày (C3, C6) có icon sort trên header. Click icon → toggle: Ascending ↑ / Descending ↓. **Mặc định sort theo C6 (Ngày điều chỉnh): xa nhất → gần nhất (descending).** Dòng mới thêm vào cuối bảng, user tự sort lại nếu muốn. Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự. Khi auto-load dữ liệu, hệ thống auto-sort theo default sort trước khi render.
- **Nhập từ file:** Áp dụng CF_02 Case 2 (không có Phạm vi). Chi tiết tham khảo UC089-094.
- **Xuất báo cáo:** Kết xuất file **Excel**. Tham chiếu: CF_04.

#### 3.4 Tiêu chí nghiệm thu (Acceptance Criteria)

- **AC1:** Auto-load: User mở form Lập/Chỉnh sửa báo cáo → hệ thống tự động load các dòng điều chỉnh từ DB. Tất cả cột Editable.
- **AC2:** Kiểm tra C2: User nhập C2 và blur, mã không tồn tại trong DB → hiển thị cảnh báo inline, không auto-fill.
- **AC3:** Auto-fill C2 hợp lệ: User nhập C2 hợp lệ và blur → hệ thống auto-fill C3→C9. Tất cả vẫn Editable.
- **AC4:** Validate C6: C6 < C3 hoặc C6 > ngày hiện tại → hiển thị lỗi inline tương ứng.
- **AC5:** Validate C7 ≠ C8: C7 giống hệt C8 (sau trim) → lỗi inline tại C8.
- **AC6:** Sort: Mặc định sort theo C6 (Ngày điều chỉnh) descending. User click icon sort trên header C3/C6 để toggle Ascending/Descending. Sort persist khi Lưu nháp.
- **AC7:** Xóa dòng: User nhấn icon Xóa trên bất kỳ dòng nào → popup xác nhận. Đồng ý → xóa + re-index STT.
- **AC8:** Empty table: Bảng có 0 dòng, user nhấn [Nộp] → chặn nộp + Toast.
- **AC9:** Concurrent edit: Last Write Wins — thao tác sau ghi đè. Cả 2 ghi Lifecycle Log. Tham chiếu: CMR_02, CF_06.

#### 3.5 Yêu cầu phi chức năng (NFR)

- **Performance:** Thời gian tải danh sách báo cáo < 3s. API timeout: 5s.
- **Security:** Phân quyền RBAC. Cách ly hoàn toàn giữa các Bộ. Audit log đầy đủ.
- **Concurrency:** Last Write Wins — thao tác sau ghi đè thao tác trước. Cả 2 ghi Lifecycle Log. Tham chiếu: CMR_02, CF_06.

---


## UC095-100.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi. Quyền truy cập được kiểm soát theo CMR_03.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Phân quyền cách ly hoàn toàn — mỗi Bộ chỉ thao tác trên báo cáo của Bộ mình. Tham chiếu: CMR_02, CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC095-100.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 97, 98, 99, 100

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Điều hướng đến màn hình xem toàn trang (toàn bộ trường Disabled). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Mở popup Vòng đời (Audit Trail). Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Excel. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Phân quyền | "Mỗi Bộ chỉ thấy báo cáo của Bộ mình" | Cách ly hoàn toàn — mỗi Bộ chỉ nhìn thấy và thao tác BC của Bộ mình. Bộ A không truy cập được BC Bộ B. | Làm rõ mô hình phân quyền |
| 2026-05-07 | 1.0 → 1.1 | Scope | Không đề cập Nhập từ file, Out of Scope | Nhập từ file áp dụng CF_02 Case 2. Bổ sung Out of Scope rõ ràng. | Bổ sung Nhập từ file + Out of Scope |
| 2026-05-07 | 1.0 → 1.1 | Dynamic Table | Không phân biệt loại dòng | 2 loại dòng: Dòng API (hệ thống auto-load C2→C9, C2-C6 Disabled, C7-C9 Enabled, không xóa) vs Dòng user thêm tay (C2 nhập thủ công, sau auto-fill C3-C6 Disabled, C7-C9 Enabled, cho xóa). | Làm rõ hành vi Dynamic Table |
| 2026-05-07 | 1.0 → 1.1 | C2 reset | Không mô tả | Xóa/sửa C2 sau auto-fill → C3-C9 clear/reset toàn bộ. | Bổ sung edge case |
| 2026-05-07 | 1.0 → 1.1 | C7==C8 error text | Chưa định nghĩa exact text | "Nội dung trước và sau điều chỉnh không được giống nhau" | Bổ sung error message |
| 2026-05-07 | 1.0 → 1.1 | C9 max length | 200 ký tự | 500 ký tự (theo CMR_06 default) | Đồng bộ chuẩn chung |
| 2026-05-07 | 1.0 → 1.1 | B2 Xóa dòng | Không phân biệt API/user, không có text popup | Chỉ hiển thị ở dòng user. Popup: "Bạn có chắc chắn muốn xóa dòng này?" | Làm rõ điều kiện + nội dung popup |
| 2026-05-07 | 1.0 → 1.1 | Lĩnh vực filter | Chưa rõ datasource | Dynamic — lấy từ giá trị user đã nhập khi lập BC | Làm rõ datasource dropdown |
| 2026-05-07 | 1.0 → 1.1 | Mã báo cáo | FDI_AIV6_[ID] | FDI_AIV6_[ID] — auto-increment, global unique, không reset. | Bổ sung logic sinh ID |
| 2026-05-07 | 1.0 → 1.1 | C6 trạng thái | Chưa phân biệt theo loại dòng | Dòng API: Disabled (auto-fill). Dòng user: Enabled. | Làm rõ trạng thái theo loại dòng |
| 2026-05-07 | 1.0 → 1.1 | C7, C8, C9 trạng thái | Chưa nêu rõ | Luôn Enabled bất kể dòng API hay user | Làm rõ trạng thái |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_6_[ID]` | `FDI_AIV6_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-14 | 1.1 → 1.2 | Filter Lĩnh vực (danh sách) | Có filter Lĩnh vực (row #3) | Xóa — không cần filter theo lĩnh vực | Client feedback. |
| 2026-05-14 | 1.2 | Lĩnh vực mặc định | Bộ Tư pháp: "HÀNH NGHỀ LUẬT SƯ"; Bộ Công thương: "THƯƠNG MẠI/NHƯỢNG QUYỀN THƯƠNG MẠI"; NHNN: "NGÂN HÀNG" | Bộ Công thương: "DẦU KHÍ"; Bộ Tư pháp: "CÔNG TY LUẬT"; NHNN: "NGÂN HÀNG NƯỚC NGOÀI" | Client feedback — cập nhật tên lĩnh vực. |
| 2026-05-14 | 1.2 | C2 validation | Text (không rõ max length) | Text free, max 50 ký tự | Client feedback — nới lỏng format + giới hạn. |
| 2026-05-14 | 1.2 | Dòng API | C2-C6 Disabled, C7-C9 Enabled, không cho xóa | Tất cả Editable, cho xóa — user chịu trách nhiệm cuối | Client feedback — cho phép hiệu chỉnh dữ liệu. |
| 2026-05-14 | 1.2 | Sort | Không có | Thêm icon sort cho C3, C6. Mặc định sort C6 descending. Persist khi Lưu nháp | Client feedback — thêm sort. |
| 2026-05-14 | 1.2 | AC + NFR | Không có | Bổ sung AC1-AC9 + NFR (Performance, Security, Concurrency) | Chuẩn hóa tài liệu. |
| 2026-05-14 | 1.2 → 1.3 | AC | Format Given/When/Then (tiếng Anh) | Viết lại tiếng Việt thuần, bỏ Given/When/Then | QC Review — chuẩn hóa ngôn ngữ AC. |
| 2026-05-14 | 1.3 → 1.4 | Quý + Năm báo cáo (form Lập) | Editable, cho phép chọn/nhập | Disabled — hiển thị quý/năm đã chọn từ màn danh sách | QC Review — kỳ đã xác định từ danh sách, không cần nhập lại. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (2 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | 1.4 → 1.5 | Filter dropdown default (row 2, 3) | Null | Tất cả (thêm option "Tất cả" đầu danh sách) | CMR_16 — mặc định hiển thị toàn bộ |
| 2026-05-22 | 1.5 | Error messages trailing `.` | Có dấu `.` cuối (C2 check, C6<C3, C6>today) | Bỏ dấu `.` cuối 3 error messages | Chuẩn hóa format error message |
| 2026-05-22 | 1.5 | Required error C7, C8 | Không có error message cụ thể | Bổ sung: "Vui lòng nhập Nội dung điều chỉnh trước/sau" | CMR_06 — required field validation |
| 2026-05-22 | 1.5 | Button state B3, B4 | Không ghi rõ trạng thái | Bổ sung "Luôn Enabled" cho Lưu nháp, Nộp báo cáo | Rule I01 — rõ ràng hóa button state |
| 2026-05-22 | 1.5 | Cột Lĩnh vực (danh sách báo cáo) | Có cột Lĩnh vực (dòng #10) | Xóa — không hiển thị trên danh sách | Client feedback — đã yêu cầu bỏ từ trước. |
