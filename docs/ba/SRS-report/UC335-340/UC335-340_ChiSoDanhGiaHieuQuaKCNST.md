# UC335-340: Các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của khu công nghiệp sinh thái

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | Mẫu A.5 |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Ban quản lý khu công nghiệp, kinh tế |
| **Đối tượng lập** | Nhà đầu tư / Tổ chức kinh tế thực hiện dự án |
| **Giao diện** | User site |
| **Ngày tạo** | 2026-05-14 |
| **Phiên bản** | 1.1 |
| **Quy tắc sinh mã báo cáo** | EZ_A5_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_01 |

---

## UC335-340.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của khu công nghiệp sinh thái
- Chức năng cho phép Nhà đầu tư/Tổ chức kinh tế truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

Ngoài phạm vi: Quy trình xét duyệt/phê duyệt báo cáo (thuộc Admin site). Quản lý cấu hình kỳ báo cáo. Nhập từ file báo cáo chi tiết (tham chiếu CF_02).

Phân quyền: Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo.

Điều kiện tiên quyết: Báo cáo này sẽ xuất hiện ở site user (Nhà đầu tư, doanh nghiệp/ tổ chức). Các doanh nghiệp sẽ nhìn thấy danh sách báo cáo.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Các chỉ số đánh giá hiệu quả KCN sinh thái

Hậu điều kiện: Hiển thị danh sách các kỳ báo cáo, cấu trúc màn hình danh sách báo cáo. Tham chiếu: CS_01.

Acceptance Criteria: Hiển thị toàn bộ các kỳ báo cáo đã được admin lập và các báo cáo mà nhà đầu tư đã nộp. Tham chiếu: CS_01.

Chức năng đáp ứng usecase số: 335, 336, 337, 338, 339, 340

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái bản ghi (Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa). Chọn nhiều giá trị. Hiển thị kết quả ngay lập tức. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn. Mặc định ở trạng thái collapse; click vào mũi tên sẽ expand ra danh sách các báo cáo của kỳ đó. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ báo cáo | Label | Null | | | Hiển thị trạng thái kỳ theo thời gian: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Button chỉ hiển thị và enable khi kỳ báo cáo ở trạng thái "Trong thời hạn", và sẽ ẩn đi khi kỳ báo cáo ở trạng thái "Chưa tới hạn" và "Qua kỳ báo cáo". Tham chiếu: CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Button chỉ hiển thị và enable khi kỳ báo cáo ở trạng thái "Trong thời hạn", và sẽ ẩn đi khi kỳ báo cáo ở trạng thái "Chưa tới hạn" và "Qua kỳ báo cáo". Khi click vào thì mở màn hình chọn/kéo thả file nhập từ file. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc EZ_A5_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Hiển thị ngày giờ thao tác gần nhất (Lưu nháp / Gửi). Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Trạng thái bản ghi. Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Hiển thị các action: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo theo trạng thái bản ghi. Tham chiếu: UC335-340.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu hiển thị:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo, mặc định collapse.
  - Sắp xếp báo cáo bên trong kỳ theo thứ tự từ mới → cũ.
  - Phân trang: Chọn hiển thị số kỳ báo cáo/trang. Tham chiếu: CMR_10.
- Lọc & Tìm kiếm:
  - Do là User Site, danh sách chỉ hiển thị báo cáo của NĐT đang login.
- Ẩn/hiện Action theo kỳ:
  - [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ báo cáo chưa bắt đầu. Tham chiếu: CF_01.

---

## UC335-340.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của khu công nghiệp sinh thái (Mẫu A.5)
- Chức năng cho phép Nhà đầu tư điền biểu mẫu dạng bảng gồm 18 chỉ số chia thành 4 section (Môi trường, Quản lý KCN, Xã hội, Kinh tế). Hệ thống tự generate bảng có sẵn các dòng khi user mở form.

Phân quyền: Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo.

Điều kiện tiên quyết: Nhà đầu tư được phân quyền lập báo cáo này và đã đăng nhập vào hệ thống.

Truy cập chức năng: Màn danh sách báo cáo (UC335-340.1) → Nhấn nút [Lập báo cáo]

Hậu điều kiện: Tùy thuộc vào action người dùng chọn (Hủy / Xem / Lưu nháp / Gửi báo cáo) sẽ có cách xử lý khác nhau. Tham chiếu: CF_01.

Acceptance Criteria: Phụ thuộc vào hành vi của Nhà đầu tư:
- Người dùng chọn Lưu nháp: Tham chiếu CF_01 → Xử lý nút [Lưu nháp]
- Người dùng chọn Xem chi tiết: Tham chiếu CF_01 → Xử lý nút [Xem chi tiết]
- Người dùng chọn Gửi báo cáo: Tham chiếu CF_01 → Xử lý nút [Gửi báo cáo]
- Người dùng chọn Hủy: Tham chiếu CF_01 → Xử lý nút [Hủy]

Chức năng đáp ứng usecase số: 335, 336

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Form nhập liệu dạng bảng, hệ thống tự generate sẵn 18 dòng chỉ số khi mở form.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **I. MÔI TRƯỜNG** | | | | | | |
| 1 | Cộng sinh công nghiệp (ENV.1) | Number | Null | x | x | Nhập số nguyên dương. Placeholder: "Nhập giá trị". Tooltip: Nhập số lượng cộng sinh công nghiệp đã thực hiện trong KCN. Tham chiếu: CMR_05. |
| 2 | Tuần hoàn tái sử dụng nước thải công nghiệp (EVN.3) | Number | Null | x | x | Nhập số dương, giá trị từ 0 - 100%. Placeholder: "Nhập giá trị từ 0 - 100%". Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%". Tooltip: Tỷ lệ phần trăm nước thải công nghiệp của các doanh nghiệp trong KCN được tái sử dụng/tuần hoàn trong và ngoài KCN theo quy định của pháp luật. Tham chiếu: CMR_05. |
| 3 | Giám sát giảm phát thải khí nhà kính (EVN.4) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Chương trình và kế hoạch cụ thể để giám sát và giảm thiểu phát thải khí nhà kính như CO2, CH4, và NOx. Tham chiếu: CMR_07. |
| 4 | Xây dựng và thực hiện cơ chế phối hợp giám sát đầu vào và đầu ra về sử dụng nguyên vật liệu, nước, năng lượng, hóa chất, chất thải, phế liệu trong KCN (ENV.5) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: NĐT thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng KCN phải xây dựng và thực hiện cơ chế phối hợp giám sát đầu vào và đầu ra về sử dụng nguyên liệu, vật liệu, nước, năng lượng, hóa chất, chất thải, phế liệu trong KCN. Tham chiếu: CMR_07. |
| 5 | Báo cáo phát triển bền vững (ENV.6) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Hàng năm NĐT thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng KCN phải công bố báo cáo thực hiện bảo vệ môi trường, trách nhiệm xã hội đối với cộng đồng xung quanh. Tham chiếu: CMR_07. |
| **II. QUẢN LÝ KHU CÔNG NGHIỆP** | | | | | | |
| 6 | Hệ thống giám sát khung về rủi ro (PM.1) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: KCN thành lập và duy trì hệ thống giám sát khung để theo dõi và lập báo cáo về các yếu tố rủi ro nguy kịch và kế hoạch ứng phó. Tham chiếu: CMR_07. |
| 7 | Kế hoạch ứng phó rủi ro (PM.2) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Cơ quan quản lý KCN có kế hoạch ứng phó với các tác động tiêu cực của biến đổi khí hậu và cập nhật 7 năm/lần (như nóng và hạn hán đỉnh điểm, các hiện tượng bão lụt). Tham chiếu: CMR_07. |
| 8 | Đơn vị hỗ trợ phát triển khu công nghiệp sinh thái (PM.3) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Ban quản lý KCN, KKT giao một đơn vị sự nghiệp công lập trực thuộc Ban quản lý hoặc một đơn vị phù hợp thực hiện chức năng xây dựng, cung cấp thông tin, cơ sở dữ liệu về sử dụng hiệu quả tài nguyên và sản xuất sạch hơn; đề xuất giải pháp và kết nối doanh nghiệp thực hiện cộng sinh công nghiệp; cung cấp dịch vụ hỗ trợ chuyển đổi hoặc đầu tư mới KCN sinh thái. Tham chiếu: CMR_07. |
| 9 | Thành lập mới khu công nghiệp sinh thái (PM.4) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: NĐT thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng KCN sinh thái đăng ký ngành, nghề thu hút đầu tư vào KCN; dự kiến mức phát thải cho từng ngành, nghề; dự kiến phương án cộng sinh công nghiệp trong KCN, phương án xây dựng và thực hiện cơ chế giám sát đầu vào, đầu ra của KCN về sử dụng nguyên liệu, vật liệu, nước, năng lượng, hóa chất, chất thải, phế liệu và phương án thực hiện trách nhiệm xã hội đối với cộng đồng xung quanh. Tham chiếu: CMR_07. |
| **III. XÃ HỘI** | | | | | | |
| 10 | Cơ sở hạ tầng xã hội phục vụ người lao động trong khu công nghiệp (SOC.3) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Cơ sở hạ tầng xã hội phục vụ người lao động (quy định tại quy hoạch xây dựng của KCN) đáp ứng yêu cầu của người lao động. Tham chiếu: CMR_07. |
| 11 | Cán bộ quản lý khu công nghiệp (SOC.5) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: NĐT thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng KCN hoặc Ban quản lý KCN, KKT có cán bộ chuyên trách về các chỉ tiêu xã hội. Tham chiếu: CMR_07. |
| 12 | Duy trì kết nối và đối thoại với cộng đồng (SOC.7) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Duy trì kinh phí chi cho kết nối cộng đồng hàng năm. Tham chiếu: CMR_07. |
| **IV. KINH TẾ** | | | | | | |
| 13 | Hợp tác kinh tế (ECO.1) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: KCN có kế hoạch phát triển liên kết hợp tác kinh tế giữa các doanh nghiệp trong KCN. Tham chiếu: CMR_07. |
| 14 | Quảng bá thông tin về phát triển khu công nghiệp sinh thái (ECO.2) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Quảng bá mô hình khu công nghiệp sinh thái. Tham chiếu: CMR_07. |
| 15 | Tối đa hóa lợi ích cho lao động địa phương (ECO.3) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: KCN có chiến lược ưu tiên sử dụng lao động địa phương. Tham chiếu: CMR_07. |
| 16 | Phát triển doanh nghiệp vừa và nhỏ (ECO.4) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: KCN tạo điều kiện cho doanh nghiệp vừa và nhỏ cung cấp dịch vụ và tạo giá trị gia tăng cho KCN. Tham chiếu: CMR_07. |
| 17 | Thúc đẩy doanh nghiệp địa phương (ECO.5) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: KCN ưu tiên sử dụng nhà cung cấp địa phương. Tham chiếu: CMR_07. |
| 18 | Giá trị dịch vụ khu công nghiệp (ECO.6) | Dropdown | Null | x | x | Giá trị: Có / Không. Placeholder: "Chọn giá trị". Tooltip: Khoản thu từ dịch vụ/phí hạ tầng đảm bảo kinh phí hoạt động cho KCN. Tham chiếu: CMR_07. |
| **Khung các Button** | | | | | | |
| B1 | Lưu nháp | Button | Null | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B2 | Gửi báo cáo | Button | Null | | | Tham chiếu: CF_01 (mục "Xử lý nút [Gửi báo cáo]"). |
| B3 | Hủy | Button | Null | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B4 | Xem chi tiết | Button | Null | | | Tham chiếu: CF_01 (mục "Xử lý nút [Xem chi tiết]"). |

---

### 3. Mô tả các xử lý của chức năng

- Khi user mở form lập báo cáo, hệ thống tự generate ra 1 bảng đã có sẵn 18 dòng với các chỉ số thuộc 4 section (Môi trường, Quản lý KCN, Xã hội, Kinh tế).
- Không có bước chọn dự án (phạm vi = Không có phạm vi).
- Mỗi NĐT chỉ lập được 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý trong mỗi kỳ.
- Validation:
  - Dòng 1 (ENV.1): Số dương.
  - Dòng 2 (EVN.3): Số dương, từ 0 - 100%. Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%".
  - Dòng 3-18: Dropdown bắt buộc chọn (Có / Không).
- Xuất báo cáo: Định dạng Docx.

---

## UC335-340.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép Nhà đầu tư thực hiện tác vụ theo trạng thái báo cáo (Lưu nháp / Yêu cầu chỉnh sửa).

Phân quyền: Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo. Hành động hiển thị theo trạng thái bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC335-340.1) → Cột Hành động → Chọn tác vụ tương ứng

Hậu điều kiện: Tùy thuộc action: Xem chi tiết → hiển thị full-page read-only (CF_07); Xóa → bản ghi bị xóa khỏi danh sách (CF_08); Nộp → chuyển trạng thái theo CMR_03; Chỉnh sửa → mở form chỉnh sửa (CF_03).

Chức năng đáp ứng usecase số: 337, 338, 339, 340

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống hệt màn hình Lập báo cáo.
- Nút [Chỉnh sửa]: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. Tham chiếu: CF_07, CMR_03.
- Nút [Hủy]: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở màn hình Xem chi tiết báo cáo. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở popup Vòng đời. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Docx. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | 1.0 → 1.1 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình 2 bước, CMCĐT_BCTK_01 | Phân loại luồng quy trình theo yêu cầu |
